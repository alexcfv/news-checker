Rus
Идеей было создать бота который определяет фейковые ли новости или нет.
На деле большой проблемой является правильность его суждений,
алгоритм не имеет выхода в интернет, определяет новость по историческим данным и в этом вся загвостка.
Фактически новость может быть ненастоящей, но слишком "резкой" как например: "наследника убили, возможно будет война",
если думать как алгоритм то вероятность события "война" когда событие "наследника убили" произошло очень велика (первая мировая так и началась).
Много чего еще зависит от качества исторических данных, в моем случае присутсвует довольно маленький датасет и в нем всего 2 класса (правдивая и ложная),
если бы было еще например такие классы как: пропаганда, манипуляция и тд, алгоритм бы определял такое довольно хорошо, т к он может выслеживать в тексте такие психологические манипуляции
Но увы, на русском языке такого качественного датасета еще нет(как минимум я не нашел)


Eng
The idea was to create a bot that determines whether news is fake or not.
In fact, the big problem is the correctness of its judgments,
the algorithm does not have access to the Internet, it determines the news based on historical data and that's the whole catch.
In fact, the news may be fake, but too "harsh" like, for example: "the heir was killed, there may be a war",
if you think like an algorithm, then the probability of the event "war" when the event "the heir was killed" occurred is very high (this is how the First World War began).
A lot of other things depend on the quality of historical data, in my case there is a rather small dataset and it only has 2 classes (true and false),
if there were also, for example, such classes as: propaganda, manipulation, etc., the algorithm would determine this quite well, since it can track down such psychological manipulations in the text
But alas, there is no such high-quality dataset in Russian yet (at least I have not found it)
