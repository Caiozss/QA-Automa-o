import { test, expect } from '@playwright/test';

test.describe('Login Testes', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://practicetestautomation.com/practice-test-login/');
  });

  test('Login com sucesso', async ({ page }) => {
    await page.fill('#username', 'student');
    await page.fill('#password', 'Password123');
    await page.click('#submit');
    await expect(page.getByText('Logged In Successfully')).toBeVisible();
  });

  test('Login com falha', async ({ page }) => {
    await page.fill('#username', 'user_erro');
    await page.fill('#password', 'senha_erro');
    await page.click('#submit');
    await expect(page.getByText('Your username is invalid!')).toBeVisible();
  });
});
