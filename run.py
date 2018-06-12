from parsers import parse
import _regexes
# this is test for DOPs typeform

ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
user_agent = parse(ua_string)
print user_agent.is_mobile # returns True
print user_agent.is_tablet # returns False
print user_agent.is_touch_capable # returns True
print user_agent.is_pc # returns False
print user_agent.is_bot # returns False
print str(user_agent) # returns "Samsung GT-I9300 / Android 4.0.4 / Android 4.0.4"
