import os

from selene import browser, have

from registration_page import RegistrationPage


def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()
    #WHEN
    registration_page.fill_first_name('Papa')
    registration_page.fill_last_name('Carlo')
    registration_page.fill_email('PapaCarlo@example.com')
    registration_page.select_gender('Male')
    registration_page.fill_number('9035645454')
    registration_page.fill_birthday('1997', 'August', '9')


    browser.element('#subjectsInput').type('ma').press_enter()

    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()

    browser.element('#uploadPicture').type(os.getcwd() + "/test.png")

    browser.element('#currentAddress').type('Ekb, Russia').click()
    browser.element('#react-select-3-input').set_value('NCR').press_tab()
    browser.element('#react-select-4-input').set_value('Delhi').press_tab()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts('Student Name Papa Carlo', 'Student Email PapaCarlo@example.com',
                                                    'Gender Male', 'Mobile 9035645454', 'Date of Birth 09 August,1997',
                                                    'Subjects Maths', 'Hobbies Sports, Reading, Music',
                                                    'Picture test.png', 'Address Ekb, Russia',
                                                    'State and City NCR Delhi'))