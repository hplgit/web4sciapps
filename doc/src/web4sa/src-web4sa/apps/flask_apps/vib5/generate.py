from parampool.generator.flask import generate
from compute import compute_gamma

generate(compute_gamma, default_field='FloatField', enable_login=True)
