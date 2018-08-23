#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from google.appengine.api import urlfetch
from datetime import datetime, date
import datetime
from decimal import *

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.out.write(template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('results.html')
        self.response.out.write(template.render())

    def post(self):

        template = env.get_template('results.html')

        def getDaysOfSemester():
            firstDay = datetime.date(2018, 8, 27)
            lastDay = datetime.date(2018, 12, 14)
            totalDays = lastDay - firstDay
            return totalDays.days

        def getTotalDays():
            todaysDate = datetime.date.today()
            lastDay = datetime.date(2018, 12, 14)
            totalDays = lastDay - todaysDate
            return totalDays.days

        # def checkSpringBreak(days):
        #     if springBreak == 'No':
        #         days = days - 7
        #     return days

        def checkThanksgiving(days):
            if thanksgiving == 'No':
                days = days - 5
            return days

        def getDollarsPerMeal(days, money):
            meals = days * 3
            dollarsPerMeal = Decimal(money) / Decimal(meals)
            dollarsPerMeal = round(dollarsPerMeal, 2)
            return dollarsPerMeal

        def getDollarsPerDay(days, money):
            dollarsPerDay = Decimal(money) / Decimal(days)
            dollarsPerDay = round(dollarsPerDay, 2)
            return dollarsPerDay

        def translatePlanToMoney(plan):
            if plan == 'L':
                return 1768;
            if plan == 'I':
                return 1772;
            if plan == 'O':
                return 1640;
            if plan == 'N':
                return 1600;

        def savedMoney(dollarsPerDay, planDollarsPerDay):
            return dollarsPerDay >= planDollarsPerDay;


        #String of L, I, O, or N
        plan = self.request.get('plan')

        #String of 'Yes' or 'No' if user will be present on Thanksgiving break
        thanksgiving = self.request.get('thanksgiving')
        #String of 'Yes' or 'No' if user will be present during Spring break
        # springBreak = self.request.get('springBreak')

        #Number of how many dollars are left on LION account
        moneyLeft = self.request.get('moneyLeft')

        totalDays = getTotalDays()

        # totalDays = checkSpringBreak(totalDays)
        totalDays = checkThanksgiving(totalDays)

        dollarsPerMeal = getDollarsPerMeal(totalDays, moneyLeft)
        dollarsPerDay = getDollarsPerDay(totalDays, moneyLeft)

        dollarsPerPlan = translatePlanToMoney(plan)
        planDollarsPerDay = getDollarsPerDay(getDaysOfSemester(), dollarsPerPlan)
        planDollarsPerMeal = getDollarsPerMeal(getDaysOfSemester(), dollarsPerPlan)

        savedMoney = savedMoney(dollarsPerDay, planDollarsPerDay)

        if (savedMoney):
            savedMoneyAnswer = "HAVE"
        else:
            savedMoneyAnswer = "HAVE NOT"

        vars = {
            'plan': plan,
            # 'springBreak': springBreak,
            'thanksgiving': thanksgiving,
            'moneyLeft': moneyLeft,
            'totalDays': totalDays,
            'dollarsPerMeal': dollarsPerMeal,
            'dollarsPerDay': dollarsPerDay,
            'dollarsPerPlan': dollarsPerPlan,
            'planDollarsPerDay': planDollarsPerDay,
            'planDollarsPerMeal': planDollarsPerMeal,
            'savedMoneyAnswer': savedMoneyAnswer,
        }

        self.response.out.write(template.render(vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler)
], debug=True)
