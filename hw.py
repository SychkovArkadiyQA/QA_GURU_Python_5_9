import os

from selene import browser, have


def test_complete_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Papa').click()
    browser.element('#lastName').type('Carlo').click()
    browser.element('#userEmail').type('PapaCarlo@example.com')

    browser.element('[name=gender][value=Male]').double_click()

    browser.element('#userNumber').type('9035645454').click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1997"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--009').click()

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