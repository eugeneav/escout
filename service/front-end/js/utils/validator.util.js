import revalidator from  'revalidator';

class Validator {

    validateSignInData(data) {
        return revalidator.validate(data, {
            properties: {
                email: {
                    type: 'string',
                    format: 'email',
                    required: true,
                    message: 'Invalid email format'
                },
                password: {
                    type: 'string',
                    required: true,
                    allowEmpty: false,
                    message: 'Invalid password format',
                }
            }
        });
    }

    validateSignUpData(data) {
        return revalidator.validate(data, {
            properties: {
                email: {
                    type: 'string',
                    format: 'email',
                    required: true,
                    message: "Invalid email format"
                },
                password: {
                    type: 'string',
                    required: true,
                    allowEmpty: false,
                    minLength: 6,
                    message: "Invalid password format"
                },
                passwordRepeat: {
                    type: 'string',
                    required: true,
                    allowEmpty: false,
                    message: "Both passwords must be the same",
                    conform: function (v) {
                        return v === data.password;
                    }

                }
            }
        });
    }
}

export default new Validator;