<?php
/**
 * Jare Example: Typograph Simple Form
 * 
 * В данном классе рассмотрен простой пример использования
 * библиотеки, когда не требуется какая-либо настройка тофов,
 * их параметров и прочего.
 * 
 * @copyright  	Copyright (c) 2009 E.Muravjev Studio (http://emuravjev.ru)
 * @license    	http://emuravjev.ru/works/tg/eula/
 * @category	Jare
 * @package 	Examples
 * @subpackage 	TypographForm
 * @author      Arthur Rusakov <arthur@emuravjev.ru>
 */
class Example_Jare_TypographForm_Simple /*extends Example_Jare_TypographForm*/
{
	/**
	 * Конструктор
	 * 
	 * Подключаем необходимые библиотеки, осуществляем основную инициализацию
	 * сценария.
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
		
		if (strlen($text) > 4) {
			/**
			 * К тексту будут применены все тофы, которые идут вместе с дистрибутивом;
			 * из текста будут удалены все HTML-коды и их эквиваленты: &nbsp;, &mdash;, ...
			 * Теги HTML из текста не будут удалены.
			 */
			require_once 'Jare/Typograph.php';
			$text = Jare_Typograph::quickParse($text);
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

$typographForm = new Example_Jare_TypographForm_Simple();
$typographForm->run();

?>