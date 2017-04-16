#ex lambda expression
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

#check with filter method and a lambda expression
message = filter(lambda char: char!='X',garbled)

print message
