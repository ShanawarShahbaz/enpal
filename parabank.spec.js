/// <reference types="cypress" />

import { faker } from '@faker-js/faker'
import { use } from 'chai'

import { UserInfo } from '../../fixtures/types'

const user: UserInfo = {
  name: 'Test ' + faker.name.fullName().replace("'", ''),
  lname: 'last '+ faker.name.lastName(),
  city: faker.address.cityName(),
  phone: faker.phone.phoneNumber('############'),
  zipCode: faker.address.zipCode('#####'),
  email: faker.name.middleName(),
  street: faker.address.streetAddress(false),
  ssn:faker.phone.number('#####')
}


describe('Parabank user details ', () => {
    let udata:any
    before(function () {
        cy.fixture('user').then(function (data) {
          udata = data;
        })
      })
      
    it('Registers a new user', () => {
        cy.visit('https://parabank.parasoft.com/parabank/index.htm')
        cy.contains('Register').click()
        cy.get('input[name="customer.firstName"]').type(user.name)
        cy.get('input[name="customer.lastName"]').type(user.lname)
        cy.get('input[name="customer.address.street"]').type(user.street)
        cy.get('input[name="customer.address.city"]').type(user.city)
        cy.get('input[name="customer.address.state"]').type(udata.State)
        cy.get('input[name="customer.address.zipCode"]').type(user.zipCode)
        cy.get('input[name="customer.phoneNumber"]').type(user.phone)
        cy.get('input[name="customer.ssn"]').type(user.ssn)
        cy.get('input[name="customer.username"]').type(user.email) 
        cy.get('input[name="customer.password"]').type(udata.Password)
        cy.get('input[name="repeatedPassword"]').type(udata.Rpassword)
        cy.get('input[name="repeatedPassword"]').should('have.value', udata.Password)
          
        cy.get('.button').eq(2).click()
        cy.log('The New user is created !');


        cy.log('Following user detials are created for you ')
        cy.log('name: '+user.name),
        cy.log('lname: '+user.lname),
        cy.log('street: '+user.street),
        cy.log('city: '+user.city),
        cy.log('zipCode:'+user.zipCode),
        cy.log('phoneNumber:'+user.phone),
        cy.log('username: '+user.email)
    
        const someArr = [{name:user.name,lastname:user.lname,street:user.street, city:user.city, state:udata.state,zipcode:user.zipCode,phonenumber:user.phone,ssn:user.ssn,username:user.email,password:udata.Password,ReapeatedPassword:udata.Rpassword}];
        cy.writeFile('cypress/fixtures/testdata.json', someArr);
        

    })
  

    it('Logs in as the newly created user', () => {
        // empty
    })

    it('Transfers money from one bank account to another', () => {
        //  empty
    })
})
