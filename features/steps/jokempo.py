import getpass
from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not


class Jogo(object):
    def __init__(self, p1=None):
        self.p1 = p1
        self.p2 = None

    def validate(self):
        val_validos = ["tesoura", "papel", "pedra"]
        if (not self.p1 in val_validos or not self.p2 in val_validos): return False
        else : return True

    def avalia(self):
        if(self.p1 == self.p2): return "Empate"

        if(self.p1 == "tesoura"):
            if(self.p2 == "papel"): return "Jogador 1"
            else: return "Jogador 2"

        if(self.p1 == "papel"):
            if(self.p2 == "pedra"): return "Jogador 1"
            else : return "Jogador 2"

        if(self.p1 == "pedra"):
            if(self.p2 == "tesoura"): return "Jogador 1"
            else : return "Jogador 2"


@given('Jogador 1 escolhe papel')
def step_given(context):
    context.jogo = Jogo('papel')

@when('Jogador 2 escolhe pedra')
def step_when(context):
    context.jogo.p2 = 'pedra'

@then('Jogador 1 vence')
def step_vence(context):
    assert_that('Jogador 1', equal_to(context.jogo.avalia()))
