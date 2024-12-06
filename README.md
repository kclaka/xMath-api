# :rocket: xMath API (Fork)
This is a fork of the [xMath API](https://github.com/cheatsnake/xMath-api), which is now deprecated. The API has been revived and is hosted at:  
**[x-math.azurewebsites.net](https://x-math.azurewebsites.net)**.

[![Website](https://img.shields.io/website?down_color=green&down_message=xMath%20API&up_color=blue&up_message=xMath%20API&url=https%3A%2F%2Fx-math.azurewebsites.net%2F)](https://x-math.azurewebsites.net)
![GitHub repo size](https://img.shields.io/github/repo-size/your-username/xMath-api?color=9cf)
![GitHub](https://img.shields.io/github/license/your-username/xMath-api?color=%235DAF83)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/your-username/xMath-api/issues)

---

## :grey_question: What is it?
The xMath API is a free API for generating random mathematical expressions. It provides the ability to get expressions for operations like addition, subtraction, multiplication, and division. You can request a specific operation or a random one.

---

## :rocket: Base URL
The API is now hosted at: https://x-math.azurewebsites.net/api
# :rocket: xMath-api
A free API for generating random mathematical expressions.

## :grey_question: How to use it?
The API provides you with the ability to get a random expression with mathematical operations such as addition, subtraction, multiplication or division. You get an object containing two numbers, an operation sign, and the result of an expression.

You can choose the operation you need or get a random operation.

#### :game_die: Random expression 
```sh
https://x-math.azurewebsites.net/api/random
```

#### :heavy_plus_sign: Only addition
```sh
https://x-math.azurewebsites.net/api/add
```

#### :heavy_minus_sign: Only subtraction
```sh
https://x-math.azurewebsites.net/api/sub
```

#### :heavy_multiplication_x: Only multiplication
```sh
https://x-math.azurewebsites.net/api/mul
```

#### :heavy_division_sign: Only division
```sh
https://x-math.azurewebsites.net/api/div
```

## :wrench: Parameters
By default, the range of numbers from 1 to 99 is set for all expressions. But you can adjust the range (for any operation) yourself using the parameters.

#### Range of generated numbers
The max and min parameters change the possible range for each number in the expression.
```sh
?max=999&min=100
```

The maxFirst and minFirst parameters change the possible range only for the first number (the second number uses the default value).
```sh
?maxFirst=256&minFirst=128
```

The maxSecond and minSecond parameters change the possible range only for the second number (does not affect division, because there the second number is randomly selected from the list of divisors of the first number).
```sh
?maxSecond=256&minSecond=128
```

#### Negative result
To get expressions that result in negative numbers, you can change the range of values using the parameters described above by adding negative numbers there.

But this will not work for the subtraction operation, because by default there the first number is always greater than the second. To fix this, you can use the parameter negative in the value 1.
```sh
https://x-math.azurewebsites.net/api/sub?negative=1
```

## :grey_exclamation: Examples

```sh
https://x-math.azurewebsites.net/api/random?max=999&negative=1
```

```sh
https://x-math.azurewebsites.net/api/mul?maxFirst=999&maxSecond=20
```

```sh
https://x-math.azurewebsites.net/api/add?max=500&minFirst=100
```



