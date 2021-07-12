Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <fname> and <lname>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

Examples:
| fname  | lname    |
| fname1 | lname1   |
| fname2 | lname2   |


Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list equal to the old list without the deleted contact


Scenario: Edit a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I edit the contact from the list
    Then the new contact list count equal to the old list count