Feature: Google Logo

Scenario: Logo presence on Google home Page
    Given launch chrome browser
    When  open google home Page
    Then  verify that the logo  present on page
    And close browser

