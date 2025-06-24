from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_login import (
    current_user,
    login_required,
)

from database import db
from models.daily import Daily

daily_bp = Blueprint("daily", __name__)


@daily_bp.route("/daily", methods=["POST"])
@login_required
def create_daily():
    data = request.get_json()
    name = data.get("name")
    data_time_str = data.get("data_time")

    if not name or not data_time_str:
        return jsonify({"message": "Nome e data_time são obrigatórios"}), 400

    try:
        data_time = datetime.strptime(data_time_str, "%d/%m/%Y %H:%M")
    except ValueError:
        return jsonify(
            {"message": "Formato de data_time inválido. Use DD/MM/YYYY HH:MM"}
        ), 400
    print(current_user.id)

    new_daily = Daily(
        name=name,
        description=data.get("description"),
        data_time=data_time,
        is_diet=data.get("is_diet"),
        user=current_user.id,
    )

    if new_daily:
        db.session.add(new_daily)
        db.session.commit()
        return jsonify({"message": "Diário criado com sucesso"})
    else:
        return jsonify({"message": "Erro ao criar o diário"}), 500


@daily_bp.route("/daily", methods=["GET"])
@login_required
def get_dailies():
    dailies = Daily.query.filter_by(user=current_user.id).all()
    print(dailies)

    return {
        "dailies": [daily.to_disc() for daily in dailies],
    }


@daily_bp.route("/daily/<int:id_daily>", methods=["GET"])
@login_required
def get_daily(id_daily):
    daily = Daily.query.get(id_daily)

    if daily.id != current_user.id:
        return jsonify(
            {"message": "Você não tem permissão para acessar este diário"}
        ), 403

    if daily:
        return {"daily": daily.to_disc()}
    else:
        return jsonify({"message": "Diário não encontrado"}), 404


@daily_bp.route("/daily/<int:id_daily>", methods=["PUT"])
@login_required
def update_daily(id_daily):
    data = request.json
    daily = Daily.query.get(id_daily)

    print(daily.to_disc())

    if daily.user != current_user.id:
        return jsonify(
            {"message": "Você não tem permissão para acessar este diário"}
        ), 403

    if daily:
        data_time_str = data.get("data_time")
        data_time = datetime.strptime(data_time_str, "%d/%m/%Y %H:%M")
        daily.name = data.get("name")
        daily.description = data.get("description")
        daily.data_time = data_time
        daily.is_diet = data.get("is_diet")
        db.session.commit()
        return jsonify({"message": "Diário atualizado com sucesso"})
    else:
        return jsonify({"message": "Diário não encontrado"}), 404


@daily_bp.route("/daily/<int:id_daily>", methods=["DELETE"])
@login_required
def delete_daily(id_daily):
    daily = Daily.query.get(id_daily)

    if daily.user != current_user.id:
        return jsonify(
            {"message": "Você não tem permissão para deletar este diário"}
        ), 403

    if daily:
        db.session.delete(daily)
        db.session.commit()
        return jsonify({"message": "Diário deletado com sucesso"})
    else:
        return jsonify({"message": "Diário não encontrado"}), 404
