# Making requests to the app
BASE_URL='https://sandbox-quickbooks.api.intuit.com'
COMPANY_ID='123145907151844'
PURCHASE_OP='/v3/company/'+COMPANY_ID+'/purchase'

# OAuth stuff
CLIENT_ID='Q09pGXudM4vOLRL2wfTe5NLbEMkZWLlWYicaGAJoBchIkgAEni'
CLIENT_SECRET='DgCyVEAXFeaQh761YGNi0Iv9HOnRKm17LtPABn2R'

REDIRECT_URI_DEV='oauth_authorized'
REDIRECT_URI_PROD='http://inventory-ba-backend.herokuapp.com/oauth_authorized'
AUTH_BASE_URL='https://appcenter.intuit.com/connect/oauth2'
ACCESS_BASE_URL='https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'
REQUEST_BASE_URL=AUTH_BASE_URL

SCOPE='com.intuit.quickbooks.accounting'
