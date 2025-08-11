import ldap

def search_user(username):
    ldap_server = "ldap://localhost"
    conn = ldap.initialize(ldap_server)

    base_dn = "dc=example,dc=com"

    # 🚨 Vulnerable: Directly embedding user input into LDAP filter
    search_filter = f"(uid={username})"

    try:
        result = conn.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
        return result
    except ldap.LDAPError as e:
        print("LDAP error:", e)
    finally:
        conn.unbind()

# Example usage - attacker can inject
#print(search_user("*)(&(objectClass=person)(uid=*))"))
