import re
import requests
validatorURL = "http://validator.nu/?out=json""&""doc="

# def validate(URL):
#      + \
#         request.quote(URL)
#     print(validatorURL)
#     req = request.Request(validatorURL)
#     req.get_method = lambda: "HEAD"
#     response = request.urlopen(req)
#     print(response.read())
#     valid = (response.getheader("X-W3C-Validator-Status") == "Valid")

#     errors = int(response.getheader("X-W3C-Validator-Errors"))
#     warnings = int(response.getheader("X-W3C-Validator-Warnings"))

#     print("Valid markup: {} (Errors: {}, Warnings: {}".format(
#         valid, errors, warnings))


# validate("http://fabilus.glab.io/frisorhemsida")
