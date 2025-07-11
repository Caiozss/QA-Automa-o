# 🧪 Portfólio de Automação de Testes - QA Caio Rodrigues

Este repositório reúne projetos práticos de automação de testes com as ferramentas mais utilizadas no mercado. Os testes estão integrados ao GitHub Actions para execução contínua (CI/CD), simulando o ambiente real de trabalho em times ágeis.

---

## 🚀 Tecnologias Utilizadas

| Ferramenta   | Tipo de Teste        | Linguagem   |
|--------------|----------------------|-------------|
| ✅ Cypress    | E2E Web              | JavaScript  |
| ✅ Playwright | E2E Web              | JavaScript  |
| ✅ Pytest     | API e Web (POM)      | Python      |
| ✅ Newman     | API (Postman Runner) | JSON        |
| ✅ GitHub Actions | CI/CD             | YAML        |

---

## 📁 Estrutura do Projeto

QA-Automa-o/
├── cypress-web-tests/
│ └── cypress/e2e/login.cy.js
├── playwright-web-tests/
│ └── tests/login.spec.js
├── pytest-api-tests/
│ ├── tests/
│ │ ├── test_api_status.py
│ │ └── selenium-project-pom/
│ │ ├── conftest.py
│ │ └── test_login.py
├── postman-api-tests/
│ └── collections/login.postman_collection.json
├── .github/workflows/
│ ├── ci-cypress.yml
│ ├── ci-playwright.yml
│ ├── ci-pytest.yml
│ └── ci-newman.yml


---
    Cypress
## Executando os testes localmente

### Cypress
```bash
cd cypress-web-tests
npx cypress open
---
    Playwright
cd playwright-web-tests
npx playwright test

    Pytest

cd pytest-api-tests
pip install -r requirements.txt
pytest

    Newman
cd postman-api-tests
newman run collections/login.postman_collection.json

    
