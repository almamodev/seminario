from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema.stats import StatsSchema
from schema.sequence import SequenceSchema
from collections import Counter
from Bio.SeqUtils import GC
from Bio.SeqUtils.MeltingTemp import Tm_NN
from marshmallow import ValidationError

blueprint = Blueprint('stats', __name__)

@blueprint.route('/stats')
class StatsView(MethodView):
    @blueprint.arguments(SequenceSchema)
    @blueprint.response(200, StatsSchema)
    def post(self, payload):
        sequence: str = payload['sequence']

        try:
            stats: dict = {
                'length': len(sequence),
                'base_counts': Counter(sequence),
                'gc_content': GC(sequence),
                'tm': Tm_NN(sequence)
            }

            return StatsSchema().load(stats)
        except (ValidationError, IndexError):
            abort(400, message='Invalid sequence')

            