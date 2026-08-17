successful_login = [
        ("admin", "Password123"),
        (" admin", "Password123"),
        ("admin ", "Password123"),
        ("user", "UserPass123")
    ]

locked_user = [
        ("locked", "Locked123")
    ]

casesensitive = [
        ("Admin", "Password123"),
        ("ADMIN", "Password123"),
        ("admin", "password123"),
        ("admin", "PASSWORD123")
    ]

empty_data = [
        ("", "Password123"),
        ("admin", ""),
    ]

out_of_boundaries = [
        ("az", "Password123"),
        ("zcasdqwezxcasdqwezxca", "Password123"),
        ("admin", "Passwor"),
        ("admin", "Password123Password123Password1")

    ]

password_length = [
        ("admin", "1234567"),
        ("admin", "1234567890123456789012345678901")
    ]

mismatch_credentials = [
        ("admin", "UserPass123")
    ]

password_whitespace = [
        ("user", " UserPass123"),
        ("user", "UserPass123 ")
    ]