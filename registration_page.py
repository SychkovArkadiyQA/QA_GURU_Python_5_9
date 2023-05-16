import os

from selene import browser, have

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self
    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self
    def select_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()
        return self
    def fill_number(self, value):
        browser.element('#userNumber').type(value)
        return self
    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--00{day}').click()

