readinteger <- function()
{ 
  i <- readline(prompt="Enter a positiv integer: ")
  if(!grepl("^[0-9]+$",i))
  {
    return(readinteger())
  }
  return(as.integer(i))
}

x <- round(runif(1) * 100, digits = 0)
guess <- -1

cat("Please, guess a number between 0 and 100.\n")

while(guess != x)
{ 
  guess <- readinteger()
  if (guess == x)
  {
    cat("Well guessed!", x, "is correct.\n")
  }
  else if (guess < x)
  {
    cat("The number is bigger!\n")
  }
  else if(guess > x)
  {
    cat("The number is smaller!\n")
  }
}