<?php
/**
 * Jare Example: Typograph Advance Form
 * 
 * Данный класс иллюстрирует, как можно настроить библиотеку
 * для более продвинутого использования: рассматривается пример
 * изменения параметров тофа, отключение тофов, а так же дополнительные
 * инструменты по работе с текстом.
 * 
 * @copyright  	Copyright (c) 2009 E.Muravjev Studio (http://emuravjev.ru)
 * @license    	http://emuravjev.ru/works/tg/eula/
 * @category	Jare
 * @package 	Examples
 * @subpackage 	TypographForm
 * @author      Arthur Rusakov <arthur@emuravjev.ru>
 */
class Example_Jare_TypographForm_Advance /*extends Example_Jare_TypographForm*/
{
	/**
	 * Конструктор
	 * 
	 * Подключаем необходимые библиотеки, осуществляем основную инициализацию
	 * сценария
	 * 
	 * @return 	void
	 */
	public function __construct()
	{
		header('Content-Type: text/html; charset=utf-8');

		// Подключаем директорию /library/ в список путей
		set_include_path(get_include_path() . PATH_SEPARATOR . '/your/path/to/library');
	}

	/**
	 * Выводим страницу с формой ввода текста
	 *
	 * @return 	void
	 */
	public function run()
	{
		$this->showHeader();
		$this->showForm();
		$this->showFooter();
	}
	
	/**
	 * HTML: вывод 'хедера'
	 *
	 * @return 	void
	 */
	public function showHeader()
	{
		echo <<<EOF
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<head>		
	<title>Jare Typograph Demo</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="keywords" content="" />
	<meta name="description" content="" />
	<style type="text/css">body{}; .typo-form{};</style>
</head>
<body>
EOF;
	}
	
	/**
	 * HTML: вывод формы
	 *
	 * Если раннее пользователем был введен текст, он будет выведен
	 * в типографированном виде в форме.
	 * 
	 * @return 	void
	 */
	public function showForm()
	{
		$text = empty($_POST['text']) ? '' : trim($_POST['text']);
		$text = stripslashes($text);
		
		/**
		 * Удаляем все HTML-теги из текста
		 * 
		 * Теги <br /> будут преобразованы в переносы строк, а комбинации
		 * тегов </p><p> - в двойной перенос строки (\n\n).
		 */
		require_once 'Jare/Typograph/Tool.php';
		$text = Jare_Typograph_Tool::removeHtmlTags($text);
		//$text = Jare_Typograph_Tool::removeHtmlTags($text, array('a', 'nobr')); // удаление всех тегов, кроме <a> и <nobr>
		
		if (strlen($text) > 4) {
			// Инициализация веб-типографа
			require_once 'Jare/Typograph.php';
			$jareTypo = new Jare_Typograph($text);
			
			// Получаем тоф 'Etc' для последующей его настройки
			$tof = $jareTypo->getTof('etc');
			
			// Получаем параметр тофа по ключу для изменения
			$param = $tof->getBaseParam('copy_replace');
			// Меняем шаблон замены с заданного на новый
			$param->setOption(Jare_Typograph_Param::KEY_PARSE_REPLACE, '&copy; ');
			
			// Сохраняем измененный параметр
			$tof->setBaseParam('copy_replace', $param);
			
			// Отключаем в тофе 'Etc' параметры для типографирования по ключу
			$tof->disableBaseParam(array('auto_links', 'acute_accent', 'email'));
			
			// Полностью отключаем тоф 'Quote': при типографирование текста он будет проигнорирован
			$jareTypo->getTof('quote')->disableParsing(true);
			
			/**
			 * После предварительной настройки можем оттипографировать текст
			 * Метод 'parse' принимает массив из имен тофов, которые будут применены к тексту
			 * Метод 'getBaseTofsNames' возвращает список имен тофов, которые идут в дистрибутиве
			 */
			//$text = $jareTypo->parse(array('etc', 'space')); // к тексту будут применены только перечисленные тофы
			$text = $jareTypo->parse($jareTypo->getBaseTofsNames());
		}
		
		$text = htmlspecialchars($text);
		
		echo <<<EOF
<h1>Введите текст для типографирования</h1>
<p>Пожалуйста, обратите внимание на то, что будет оттипографирован текст, содержащий более 4 (четырех) символов.</p>
<form action="" method="post">
<div class="typo-form">
	<textarea name="text" id="text" cols="60" rows="10">$text</textarea><br />
	<input type="submit" value="Типографировать" />&nbsp;&nbsp;<input type="button" value="Очистить поле" onclick="document.getElementById('text').value = '';" />
</div>
</form>
EOF;
	}
	
	/**
	 * HTML: вывод 'футера'
	 *
	 * @return 	void
	 */
	public function showFooter()
	{
		echo <<<EOF
</body>
</html>
EOF;
	}
}

$typographForm = new Example_Jare_TypographForm_Advance();
$typographForm->run();

?>