Feature: IMDb movie search

    To watch the movie a person wants
    To find it on the IMDb website
    And make sure it is expected one

  Scenario Outline: Search for <name>
    Given person open IMDb website
    When person enter the movie <name> in the search bar
    Then search results are shown and <movie> is presented
    And person open <movie> page and see the <title>
    And one of the directors is <director>
    And rating is valid

    Examples:
      | name         | movie                           | title                              | director         |
      | White Collar | White Collar (2009) (TV Series) | White Collar (TV Series 2009–2014) | Jeff Eastin      |
      | I Am Legend  | I Am Legend (2007)              | I Am Legend (2007)                 | Francis Lawrence |
