from flask import Blueprint, jsonify, request

bp = Blueprint('routes', __name__)

@bp.route('/api/v1/health')
def health():
    return jsonify({'status': 'ok'})

@bp.route('/api/v1/todos', methods=['GET'])
def get_todos():
    return jsonify([{
            "id": 1,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2026-02-27T18:00:00",
            "created_at": "2026-02-20T14:00:00",
            "updated_at": "2026-02-20T14:00:00"
        }])

@bp.route('/api/v1/todos/<int:id>', methods=['GET'])
def test_get_todo_by_id(id):
    return jsonify({
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2026-02-27T18:00:00",
            "created_at": "2026-02-20T14:00:00",
            "updated_at": "2026-02-20T14:00:00"
        })

@bp.route('/api/v1/todos', methods=['POST'])
def create_todo():
    return jsonify({
            "id": 1,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2026-02-27T18:00:00",
            "created_at": "2026-02-20T14:00:00",
            "updated_at": "2026-02-20T14:00:00"
        }), 201

@bp.route('/api/v1/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    return jsonify({
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2026-02-27T18:00:00",
            "created_at": "2026-02-20T14:00:00",
            "updated_at": "2026-02-20T14:00:00"
        })

@bp.route('/api/v1/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2026-02-27T18:00:00",
            "created_at": "2026-02-20T14:00:00",
            "updated_at": "2026-02-20T14:00:00"
        })