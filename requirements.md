# Requirements List

### Use cases
- A user wants to execute buy and sell orders of different types quickly and efficiently 
- Orders should be constructed and placed in an atomic manner 
- A user can interact with all API elements in a single "session"
- A user wants to query the API for up-to-date market information
- A user wants to interact with thier portfolio to see thier assets 
- A user wants to build market anaylsis applications via interfacing with the API 
- Instruments (e.g Stock, Bond, Investment, Index fund, etc..) should be represented distincly
- A user should be able to end a session (i.e logout) with API calls


### Inputs
- User should not have to input a confounding set of parameters on each method call 
- Should be able to take in string represtations
- User should be able to pass in objects as parameters (e.g placing an order on an stock obj.)


### Outputs
- Money should be represented, clearly and directly correlate with the rounding of money
  standardized in the Robinhood platform.
- Values returned to the user should be clearly defined with key-value pairs 
- Values returned to the user should be up to date to most accurately represent the state of the user 
