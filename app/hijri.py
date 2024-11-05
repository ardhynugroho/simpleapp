import functools

from flask import Blueprint, request, jsonify

bp = Blueprint('hijri', __name__, url_prefix='/hijri')

from hijridate import Hijri, Gregorian

ymdText = ("year", "month", "day")

@bp.route("today", methods=["GET"])
def today():
    h = Hijri.today()
    return jsonify(dict(zip(ymdText,h.datetuple())))

@bp.route("/gtoh", methods=["GET"])
def gtoh():
    try:    
        y = int(request.args.get('y'))
        m = int(request.args.get('m'))
        d = int(request.args.get('d'))
    except KeyError:
        return "Error", 404
    
    h = Gregorian(y, m, d).to_hijri()
    return jsonify(dict(zip(ymdText, h.datetuple())))

@bp.route("/htog", methods=["GET"])
def htog():
    try:    
        y = int(request.args.get('y'))
        m = int(request.args.get('m'))
        d = int(request.args.get('d'))
    except KeyError:
        return "Error", 404
    
    g = Hijri(y, m, d).to_gregorian()
    return jsonify(dict(zip(ymdText, g.datetuple())))
