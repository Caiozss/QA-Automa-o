describe('Login flows', () => {
  beforeEach(() => {
    cy.visit('https://practicetestautomation.com/practice-test-login/');
  });

  it('login com sucesso', () => {
    cy.get('#username').type('student');
    cy.get('#password').type('Password123');
    cy.get('#submit').click();
    cy.contains('Logged In Successfully').should('be.visible');
  });

  it('login com falha', () => {
    cy.get('#username').type('user_errado');
    cy.get('#password').type('errado');
    cy.get('#submit').click();
    cy.get('#error').should('contain', 'Your username is invalid!');
  });
});
