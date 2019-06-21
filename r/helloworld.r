library("RSelenium")

readr_home <- "https://www.readr.tw/"

remDr <- remoteDriver(
  remoteServerAddr = "localhost",
  port = 4444,
  browserName = "chrome")

remDr$open()

remDr$navigate(readr_home)

remDr$close()