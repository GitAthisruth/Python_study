# An Example Webapp

# 1. Client-side code(javaScript)
# 2. A data store(ex. mySQL server)
# 3. Backend app

#    4. Routing 
#    5. HTTP,etc Requests
#    6. API to expose data
#    7. Database calls
#    8. Authentication



# The Monolith


# Pros

# 1. Easy access to other code 
# 2. Centralized models in single data store(easy to backup).
# 3. Lower devops overhead.

# Cons

# 1. Scaling one thing == scaling everything
# 2. Easy to end up with "spaghetti" code,with tangled dependencies and tight coupling, so can be dangerous to change or upgrade.
# 3. Can have long deploy cycle. 


# Microservices

# 1. Small,isolated fuctionality
# 2. Independently deployable, upgradable, scalable.
# 3. Functionality exposed over network layers(HTTP,RPC).
# 4. Decentralized data stores(many different databases e.g.)
# 5. Focus on services/developer/team independence.