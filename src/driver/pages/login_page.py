from driver import actions


def preencher_login(driver, login, senha):
    driver.find_element(
        "Usuário"
        ).send_keys(login)
    
    driver.find_element(
        "Senha"
        ).send_keys(senha)
    
    driver.find_element(
        "Entrar"
        ).click()
    
actions.clicar
    
