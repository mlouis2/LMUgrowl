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
<<<<<<< HEAD
    # delete later
    def get(self):
        template = env.get_template('results.html')
        self.response.out.write(template.render())
    # delete later

    def post(self):

        template = env.get_template('results.html')

        def getDaysOfSemester():
            firstDay = datetime.date(2017, 8, 28)
            lastDay = datetime.date(2017, 12, 15)
            totalDays = lastDay - firstDay
            return totalDays.days

        def getTotalDays():
            todaysDate = datetime.date.today()
            lastDay = datetime.date(2017, 12, 15)
            totalDays = lastDay - todaysDate
            return totalDays.days

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

        def getPointsPerWeek(days, points):
            weeks = days / 7
            pointsPerWeek = Decimal(points) / Decimal(weeks)
            #Whole number if there's a minimum of one com tom per week
            if pointsPerWeek > 1:
                pointsPerWeek = int(points) / int(weeks)
            #Decimal if less than one, so that it doesn't just say zero
            else:
                pointsPerWeek = round(pointsPerWeek, 1)
            return pointsPerWeek

        def translatePlanToMoney(plan):
            if plan == 'L':
                return 1792;
            if plan == 'I':
                return 1694;
            if plan == 'O':
                return 1559;
            if plan == 'N':
                return 1500;

        def translatePlanToPoints(plan):
            if plan == 'L':
                return 48;
            if plan == 'I':
                return 24;
            if plan == 'O':
                return 16;
            if plan == 'N':
                return 0;

        #String of L, I, O, or N
        plan = self.request.get('plan')
        #String of 'Yes' or 'No' if user will be present on Thanksgiving break
        thanksgiving = self.request.get('thanksgiving')
        #Number of how many dollars are left on LION account
        moneyLeft = self.request.get('moneyLeft')
        #Number of how many points are left on LION account
        pointsLeft = self.request.get('pointsLeft')

        totalDays = getTotalDays()
        totalDays = checkThanksgiving(totalDays)

        dollarsPerMeal = getDollarsPerMeal(totalDays, moneyLeft)
        dollarsPerDay = getDollarsPerDay(totalDays, moneyLeft)

        pointsPerWeek = getPointsPerWeek(totalDays, pointsLeft)

        dollarsPerPlan = translatePlanToMoney(plan)
        planDollarsPerDay = getDollarsPerDay(getDaysOfSemester(), dollarsPerPlan)
        planDollarsPerMeal = getDollarsPerMeal(getDaysOfSemester(), dollarsPerPlan)
        pointsPerPlan = translatePlanToPoints(plan)
        planPointsPerWeek = getPointsPerWeek(getDaysOfSemester(), pointsPerPlan)

        vars = {
            'plan': plan,
            'thanksgiving': thanksgiving,
            'moneyLeft': moneyLeft,
            'pointsLeft': pointsLeft,
            'totalDays': totalDays,
            'dollarsPerMeal': dollarsPerMeal,
            'dollarsPerDay': dollarsPerDay,
            'pointsPerWeek': pointsPerWeek,
            'dollarsPerPlan': dollarsPerPlan,
            'pointsPerPlan': pointsPerPlan,
            'planDollarsPerDay': planDollarsPerDay,
            'planDollarsPerMeal': planDollarsPerMeal,
            'planPointsPerWeek': planPointsPerWeek
        }

        self.response.out.write(template.render(vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler)
], debug=True)
