from django.test import TestCase

# Create your tests here.
d = '/*jsonp*/s7jsonResponse({"set":{"pv":"1.0","type":"media_set","n":"lanebryantProdATG/355049_0000030290_ms","item":[{"i":{"n":"lanebryantProdATG/355049_0000030290"},"s":{"n":"lanebryantProdATG/355049_0000030290"},"dx":"1154","dy":"1500","iv":"uDdTL2"},{"i":{"n":"lanebryantProdATG/355049_0000030290_alt1"},"s":{"n":"lanebryantProdATG/355049_0000030290_alt1"},"dx":"1154","dy":"1500","iv":"_JkSX3"},{"i":{"n":"lanebryantProdATG/355049_0000030290_Back"},"s":{"n":"lanebryantProdATG/355049_0000030290_Back"},"dx":"1154","dy":"1500","iv":"psgTf1"}]}},"0000030290");'
import re

print(re.findall('{.*}', d)[0])