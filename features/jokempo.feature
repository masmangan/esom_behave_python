Feature: Jogo de Jokempo

    Scenario: Jogador 1 escolheu papel 
        Given Jogador 1 escolhe papel
        When Jogador 2 escolhe pedra
        Then Jogador 1 vence
