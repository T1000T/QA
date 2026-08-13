# InnovaCRM v1.0.0 — Authentication Requirements
1. Username is required.
2. Username must contain 3–20 characters.
3. Username comparison is case-sensitive.
4. Leading/trailing username whitespace should be ignored.
5. Password is required.
6. Password must contain 8–30 characters.
7. Password comparison is case-sensitive.
8. Spaces are valid password characters.
9. Invalid credentials display `Invalid username or password.`
10. Do not reveal whether username or password was incorrect.
11. Locked accounts cannot log in.
12. Locked accounts display a clear locked-account message.
13. Successful login displays a success message and navigates to dashboard.
14. Password is masked by default.
15. Show/Hide toggles password visibility.
16. Forgot Password displays a confirmation message.
17. Remember Me keeps the user logged in after refresh.
18. Without Remember Me, the session should not persist after the browser session ends.
19. Logout clears the active session.
20. Logout redirects to login.
21. Without a valid session, dashboard access redirects to login.
22. Dashboard displays username and role.
23. Dashboard displays customer, pending-order, and revenue cards.