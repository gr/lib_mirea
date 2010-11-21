<?php
/*
| Консольный типограф работает следующим образом
| Запускаем PHP скрипт с 2 параметрами: 
|    input_file_name - текстовый файл, в котором лежит текст нуждающийся в типографировании
|    output_file_name - название файла, в который будет находиться типографированный текст
|  *ПРИМЕЧАНИЕ output_file_name и input_file_name могут содержать только имена файлов, 
|   которые должны находится в той же папке чтои этот файл.
|   Это сделано для того, что бы не писать полные пути при запуске скриптат из другой директории
| Общий синтаксис:
|   php typo.php [<input_file_name>] [<output_file_name>]
| По дефолту <input_file_name> = in; <output_file_name> = out
*/

// установка дефолтовых параметров
  if (!isset($argv[1])) $argv[1] = 'in';
  if (!isset($argv[2])) $argv[2] = 'out';

// добавляем путь к библиотекам типографа
  set_include_path(get_include_path() . PATH_SEPARATOR . dirname(__FILE__).'/library');
  
// подключаем библиотеки типографа  
  require_once 'Jare/Typograph.php';
  require_once 'Jare/Typograph/Tool.php';
  
// загружаем текст из входного файла
  $text = file_get_contents(dirname(__FILE__).'/'.$argv[1]);

  $jareTypo = new Jare_Typograph($text);
  
  //$text = Jare_Typograph_Tool::removeHtmlTags($text);
  //$text = Jare_Typograph_Tool::removeHtmlTags($text, array('a', 'nobr')); // удаление всех тегов, кроме <a> и <nobr>
  	
  // Получаем тоф 'Etc' для последующей его настройки
  $tof = $jareTypo->getTof('etc');
  
  // Получаем параметр тофа по ключу для изменения
  //$param = $tof->getBaseParam('copy_replace');
  // Меняем шаблон замены с заданного на новый
  //$param->setOption(Jare_Typograph_Param::KEY_PARSE_REPLACE, '&copy; ');
  
  // Сохраняем измененный параметр
  //$tof->setBaseParam('copy_replace', $param);
  
  // Отключаем в тофе 'Etc' параметры для типографирования по ключу
  $tof->disableBaseParam(array('auto_links', 'paragraphs'));
  
  // Полностью отключаем тоф 'Quote': при типографирование текста он будет проигнорирован
  //$jareTypo->getTof('quote')->disableParsing(true);
  
  $text = $jareTypo->parse($jareTypo->getBaseTofsNames());
  
// И применяем быстрое типографирование (с использованием всех правил)
  /*
  require_once 'Jare/Typograph.php';
  $text = Jare_Typograph::quickParse($text);
  */
  
  file_put_contents(dirname(__FILE__).'/'.$argv[2],$text);

?>