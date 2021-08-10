# geekyshows Module

import Admin.service
Admin.service.admin_service()

import Admin.product
Admin.product.admin_product()

import Admin.Common.header
Admin.Common.header.admin_common_header()

import Tech.work
Tech.work.tech_work()
print("hi")


# ab from method se karenge
from Admin import service
service.admin_service()

from Admin.Common import header
header.admin_common_header()		#header file ko access kr rhe hai

from User import profile
profile.user_profile()			#user_profile ko access kiya

##kisi function ya variable ko direct access karne k liye
from Admin.service import admin_service
admin_service()

from Admin.Common.header import admin_common_header
admin_common_header()

## import all wala karna hai
from Admin import *		# Admin k ander init file me jao toofan macha do
product.admin_product()
service.admin_service()

#ab hum subpackage dekhte hai
from Admin.Common import *
footer.admin_common_footer()
header.admin_common_header()	# ab subpackage k ander init file se accessible bnao

#last time work module ko access karne ka
from Tech import work
work.tech_work()
work.request.user_request()










