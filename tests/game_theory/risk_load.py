from mango.game_theory import risk_load_multiplier


def test_rl_multiplier():
    res = risk_load_multiplier(return_on_marginal_surplus=.2, standard_normal_multiplier=2)

    assert .33 == round(res, 2)
