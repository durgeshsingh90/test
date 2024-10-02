2024-10-02 13:16:17,409 [INFO] slot_booking: entering add_cron_job
2024-10-02 13:16:17,409 [DEBUG] paramiko.transport: starting thread (client mode): 0x78dc7f50
2024-10-02 13:16:17,420 [DEBUG] paramiko.transport: Local version/idstring: SSH-2.0-paramiko_3.4.0
2024-10-02 13:16:17,470 [DEBUG] paramiko.transport: Remote version/idstring: SSH-2.0-OpenSSH_8.1
2024-10-02 13:16:17,470 [INFO] paramiko.transport: Connected (version 2.0, client OpenSSH_8.1)
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: === Key exchange possibilities ===
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: kex algos: curve25519-sha256, curve25519-sha256@libssh.org, ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521, diffie-hellman-group-exchange-sha256, diffie-hellman-group16-sha512, diffie-hellman-group18-sha512, diffie-hellman-group14-sha256, diffie-hellman-group14-sha1, kex-strict-s-v00@openssh.com
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: server key: rsa-sha2-512, rsa-sha2-256, ssh-rsa, ecdsa-sha2-nistp256, ssh-ed25519
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: client encrypt: aes128-ctr, aes192-ctr, aes256-ctr
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: server encrypt: aes128-ctr, aes192-ctr, aes256-ctr
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: client mac: umac-64-etm@openssh.com, umac-128-etm@openssh.com, hmac-sha2-256-etm@openssh.com, hmac-sha2-512-etm@openssh.com, hmac-sha1-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, hmac-sha2-256, hmac-sha2-512, hmac-sha1
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: server mac: umac-64-etm@openssh.com, umac-128-etm@openssh.com, hmac-sha2-256-etm@openssh.com, hmac-sha2-512-etm@openssh.com, hmac-sha1-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, hmac-sha2-256, hmac-sha2-512, hmac-sha1
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: client compress: none, zlib@openssh.com
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: server compress: none, zlib@openssh.com
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: client lang: <none>
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: server lang: <none>
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: kex follows: False
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: === Key exchange agreements ===
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: Strict kex mode: True
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: Kex: curve25519-sha256@libssh.org
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: HostKey: ssh-ed25519
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: Cipher: aes128-ctr
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: MAC: hmac-sha2-256
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: Compression: none
2024-10-02 13:16:17,472 [DEBUG] paramiko.transport: === End of kex handshake ===
2024-10-02 13:16:17,640 [DEBUG] paramiko.transport: Resetting outbound seqno after NEWKEYS due to strict mode
2024-10-02 13:16:17,640 [DEBUG] paramiko.transport: kex engine KexCurve25519 specified hash_algo <built-in function openssl_sha256>
2024-10-02 13:16:17,648 [DEBUG] paramiko.transport: Switch to new keys ...
2024-10-02 13:16:17,648 [DEBUG] paramiko.transport: Resetting inbound seqno after NEWKEYS due to strict mode
2024-10-02 13:16:17,648 [DEBUG] paramiko.transport: Got EXT_INFO: {'server-sig-algs': b'ssh-ed25519,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521'}
2024-10-02 13:16:17,648 [DEBUG] paramiko.transport: Adding ssh-ed25519 host key for A5CVAP1004: b'17e13c6335e42505c5aff90d6c66a99d'
2024-10-02 13:16:17,681 [DEBUG] paramiko.transport: Trying discovered key b'3a87564dd10cee3c6c5afd1deb619f79' in C:\Users\f94gdos/.ssh/id_rsa
2024-10-02 13:16:17,720 [DEBUG] paramiko.transport: userauth is OK
2024-10-02 13:16:17,720 [DEBUG] paramiko.transport: Finalizing pubkey algorithm for key of type 'ssh-rsa'
2024-10-02 13:16:17,720 [DEBUG] paramiko.transport: Our pubkey algorithm list: ['rsa-sha2-512', 'rsa-sha2-256', 'ssh-rsa']
2024-10-02 13:16:17,720 [DEBUG] paramiko.transport: Server-side algorithm list: ['ssh-ed25519', 'ssh-rsa', 'rsa-sha2-256', 'rsa-sha2-512', 'ssh-dss', 'ecdsa-sha2-nistp256', 'ecdsa-sha2-nistp384', 'ecdsa-sha2-nistp521']
2024-10-02 13:16:17,720 [DEBUG] paramiko.transport: Agreed upon 'rsa-sha2-512' pubkey algorithm
2024-10-02 13:16:17,760 [INFO] paramiko.transport: Auth banner: b'The computer you are logging into and the systems to which it is connected (collectively Systems) are proprietary corporate systems that contain confidential and proprietary information.  The owner will pursue any and all available legal remedies to address unauthorized users.  All use of the system is subject to monitoring.  By proceeding further you indicate your consent to such monitoring.\n'
2024-10-02 13:16:17,760 [INFO] paramiko.transport: Authentication (publickey) failed.
2024-10-02 13:16:17,760 [WARNING] django.request: Forbidden: /slot_booking/add-cron-job/
