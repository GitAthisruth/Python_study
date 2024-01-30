# import nameko

# from nameko import rpc




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

#Microservice Complexity

# 1. Complexity doesn't disappear...it relocates.
# 2. More complex with microservices:
    
#     a. Authentication
#     b. Devops:Provisioning and deployment
#     c. Speed of calls(local vs. remote)
#     d. Managing backups
#     e. Service discoverability.


# Nameko 

# A python framework for creating microservices.

#     1. Library of utilities for building and running microservices.
#     2. CLI(command line interface) for easily running and interacting with services (nameko run/shell)
#     3. Way of thinking about dependencies and application logic that encourages microservices approach. 


# Nameko services

# Microservices are classes with:
#  1. a "name" attribute.
#  2. dependency attributes
#  3. methods with entrypoint decorators.


# class HelloWorldService(object):
#     name = 'hello_world_service'

#     dependency = SomeDependency()

#     @rpc
#     def say_hello(self):
#         return 'Hello world'
# rpc - Remote Procedure Call 


# n.rpc.hello_world_service.say_hello()
    
# print(HelloWorldService.say_hello())

# How does the client actually call the service?

# RabbitMQ

# A message broker implementing the Advanced Messaging Queue Protocol(AMQP), an open messaging protocol.

# Namenkolature

# Entrypoint: Exposes a method,often by monitoring an external entity(e.g. a queue)

# Dependencies: "Gateways" to other code, not managed by the service(other services,databases,APIs)

# Workers:Instance of a service class.Dependencies are replaced with result of 'get_dependency'.

# Example 1: HTTP

# 1. GET and POST methods supported
# 2. Decorators takes a method and route, with variables.
# 3. Multiple decorators can be placed on the same method
# 4. Build on top of Werkzeug(request/response objects)

"""

service-1


"""

# import nameko

# from nameko import rpc

# import json
# from nameko.web.handlers import http

# class HttpService(object):
#     name = "multiply_service"
#     @http("GET",'/multiply/<int:first>/<int:second>')
#     def get_method(self,request,first,second):
#         third = int(request.args.get('third',1))
#         return json.dumps({'value':first*second*third})


# Example 2: RPC 

# 1. Stands for "Remote procedure call".
# 2. Nameko implements RPC over AMQP.
# 3. rpc decorator: exposes method.
# 4. RpcProxy:easily inject other rpc-exposed dependency.
# 5. ClusterRpcProxy:allows non-nameko clients to make rpc calls to a cluster.



# service_2

# Example of rpc extension


from nameko.rpc import rpc

class GreeterService(object):
    name = 'greeter_service'

    @rpc
    def greet(self,name):
        """Return a string greeting using the passed name
            :param name: 'str' name of person to greet
        """
        return u'Hello {}!'.format(name)
    
    # u in front of the string values means the string is a Unicode string. Unicode is a way to represent more characters than normal ASCII can manage.