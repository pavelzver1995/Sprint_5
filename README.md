# Sprint_5

## Описание проекта
Набор автоматизированных тестов для веб-сервиса Stellar Burgers — платформы для создания космических бургеров на заказ.

## Структура тестового покрытия

### Модуль регистрации (`test_registration.py`)
- Проверка успешной регистрации нового пользователя - `TestCheckNewRegister.test_registration`
- Валидация ошибки при использовании существующего аккаунта - `TestCheckingCreationExistingAccount.test_existing_account`
- Проверка обязательности поля "Имя" - `TestCheckRegisterNoName.test_registration_no_name`
- Валидация минимальной длины пароля - `TestCheckingErrorPassword.test_error_password`
- Проверка обязательности поля "Пароль" - `TestCheckingNoPassword.test_no_password`

### Модуль авторизации (`test_check_exit.py`)
- Авторизация через главную кнопку "Войти в аккаунт" - `TestBigMainButton.test_check_entrance_by_big_button`
- Вход через раздел личного кабинета - `TestCheckRegister.test_login_password_recovery`
- Авторизация со страницы регистрации - `TestCheckEntranceFromRecoveryPage.test_button_inscription_login`
- Вход через страницу восстановления пароля - используется фикстура `start_from_recovery_page`
- Корректный выход из системы - `TestButtonCheckExit.test_check_loging_out`

### Модуль личного кабинета (`test_move_to_personal_accaunt.py`)
- Проверка перехода в профиль пользователя - `TestCheckPageProfile.test_transition_to_profile`
- Возврат в конструктор из личного кабинета - `TestTransitionByConstructor.test_check_transition_by_constructor`
- Навигация через логотип - `TestTransitionByLogo.test_transition_by_logo`
- Тестирование выхода из учетной записи - `TestButtonCheckExit.test_check_logging_out`

### Модуль конструктора бургеров (`test_move_to_desing.py`)
- Проверка работы раздела "Булки" - `TestCheckChapterBread.test_check_chapter_bread`
- Тестирование раздела "Соусы" - `TestCheckChapterSauce.test_check_chapter_sauce`
- Проверка раздела "Начинки" - `TestCheckChapterFillings.test_check_chapter_fillings`

## Инструкция по запуску
Для выполнения тестового прогона используйте команду:
```bash
pytest tests/ -v# Sprint_3
