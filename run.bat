pytest -s -v -m "sanity" -- html=./Reports/report.html testCases/ --browser chrome

rem pytest -s -v -m "sanity or Regression" -- html=./Reports/report.html testCases/ --browser- chrome
