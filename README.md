# equilibrium

**Equilibrium** - это скриптовой строго типизированный язык программирования, написанный на Python


![Equilibrium](https://sun9-76.userapi.com/58uslEXwTUlFP1BN7bzqR4QomO7rrRzvjKDPyg/Z9PPkEbGMlA.jpg "Equilibrium :)")

# Переменные

Есть 6 типов данных :
  - int(целочисленное число)
  
  - string(строка)
  
  - array(список)
  
  - float(дробное число)
  
  - char(символ)
  
  - bool(булево значения)
  
  Пример :
  
  `int n := 10`
  
  `string name := 'Renat'`
  
  `array random := ['Gosha','Equilibrium',17]`
  
  `float pi := 3.14`
  
  `char symvol := 'b'`
  
  `bool step := bad`

# Функции

**Функция run для вывода в консоль**

Пример : `write => 'Hello World'`

**Функция sleep для ожидания**

Пример : `sleep => 1`

**Функция scan для пользовательского ввода с клавиатуры**

Пример : `int old := scan()`

**Функция random для случайного числа**

Пример : `int random := random(1,100)`

**Функция coinflip для подбрасывания монетки**
Переменная должна быть типа `string`

Пример : `string сoin := coinflip()`

`Output : Решка`

# Ветвления if и else

Пример : 

`if x > 3 1{`

  `write => 'x > 3'`

`}`
  
`else 1{`

  `write => 'Fizz'`
  
`}`

# Циклы range и for

Примеры :

`for (i=1,i < 10, +1) 1{`

`write => i`

`}`


`range 10 1{`

`write => 'Привет, мир!'`

`}`

# Функции

Пример создания функции :

`def abc() 1{`

`write => 'abc'`

`}`

Пример вызова :

`def_abc()`

# Работа со временем 
  Для работы библиотеки нужно импортировать её командой include time

  - time_unix() -> функция которая возвращает(тип str) unix время(время с 1970 в секундах)
  
  - time_month() -> функция возвращает дату(тип str) в формате месяц/день/год
  
  - time_day() -> функция возвращает время(тип str) в формате час:минуты

# Работа с файлами
  Для инициализации класса библиотеки нужно создать файл, а потом производить над ним манипуляции
  
  Также нужно импортировать библиотеку командой include files
  
  - cfile() -> функция, отвечает за создание файла, один аргумент(название файла с расширением)

  - wfile() -> функция,отвечает за запись файла, один аргумент(текст записи)
  
  - rfile() -> метод, который присваивается переменной или другому методу. Читает файл по строкам
  
  - dfile -> удаляет файл, один аргумент(названия файла, тип данных str)
    
  - ufile -> обновляет отдельную строку файла, первый аргумент номер строки(тип данных int) второй аргумент строка для замены
  
 # Работа с HTTP запросами
Для работы библиотеки нужно импортировать её командой include query

- post(url,params) -> функция, отвечает за запрос post, url - ссылка на сайл, params - параметры
 
- get(url,params) -> функция, отвечает за запрос get, url - ссылка на сайл, params - параметры
  
 # Парсер
 Для инициализации класса библиотеки нужно подключить сайт
 
 Также нужно импортировать библиотеку командой include parser
 
 - cparser -> метод, которая отвечает за создание подключения к сайту
 
 - get_xpath -> функция, которая возвращает по пути xpath элемент на сайте

# Equilibrium Web

![Equilibrium](https://sun9-69.userapi.com/GQHmrgb8vyYYbotSiohG2at_St8YzyOhUPSfRA/1WeUFCvXaC8.jpg "Equilibrium :)")

Для вывода данных в web версии используется функция run

Пример :

  run 'Hello, World!'
  
# Equilibrium API

![Equilibrium](https://sun9-74.userapi.com/impf/xQVEuf73dVqEQqWa8J5w5YPoZjTU6_U1MxIeZQ/3cDryq7aTAo.jpg?size=1559x578&quality=96&proxy=1&sign=43e3066a783670e9ada66de49fd61975&type=album "Eq :)")

Для того что бы получить ответ от сервера, нужно сделать get запрос на /api/ и в params указать JSON с ключём code и значением в виде твоего кода,сервер вернёт ответ в виде JSON

Пример :

`params = {'code': "run 3 > 2",}`

`r = requests.get(url=url, params=params)`

`print(r.text)`

# Варнинги

**IndexWarning** - ошибки с индексом списков

**TypeWarning** - ошибки с типом данных 

**ValueWarning** - ошибки со значением

**SyntaxWarning** - ошибки синтаксиса

**KeyWarning** - ошибка с ключём(массив или строка)

**FileExistsWarning** - ошибка когда файл не найден

**OSWarning** - ошибка с операционной системой(к примеру не найдено файла, который нужно удалить)

**ZeroDivisionError** - ошибка с делением на ноль

**FileConnectionError** - пропало подключения с файлом, нужно инициализировать ещё раз

**LibraryClassNoImport** - библиотека не подключена

**FileNoEquilibrium** - открываемый файл не является файлом Equilibrium






                   
