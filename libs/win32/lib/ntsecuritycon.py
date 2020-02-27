# Hacked from winnt.h

DELETE = (65536)
READ_CONTROL = (131072)
WRITE_DAC = (262144)
WRITE_OWNER = (524288)
SYNCHRONIZE = (1048576)
STANDARD_RIGHTS_REQUIRED = (983040)
STANDARD_RIGHTS_READ = (READ_CONTROL)
STANDARD_RIGHTS_WRITE = (READ_CONTROL)
STANDARD_RIGHTS_EXECUTE = (READ_CONTROL)
STANDARD_RIGHTS_ALL = (2031616)
SPECIFIC_RIGHTS_ALL = (65535)
ACCESS_SYSTEM_SECURITY = (16777216)
MAXIMUM_ALLOWED = (33554432)
GENERIC_READ = (-2147483648)
GENERIC_WRITE = (1073741824)
GENERIC_EXECUTE = (536870912)
GENERIC_ALL = (268435456)

# file security permissions
FILE_READ_DATA=            ( 1 )
FILE_LIST_DIRECTORY=       ( 1 )
FILE_WRITE_DATA=           ( 2 )
FILE_ADD_FILE=             ( 2 )
FILE_APPEND_DATA=          ( 4 )
FILE_ADD_SUBDIRECTORY=     ( 4 )
FILE_CREATE_PIPE_INSTANCE= ( 4 )
FILE_READ_EA=              ( 8 )
FILE_WRITE_EA=             ( 16 )
FILE_EXECUTE=              ( 32 )
FILE_TRAVERSE=             ( 32 )
FILE_DELETE_CHILD=         ( 64 )
FILE_READ_ATTRIBUTES=      ( 128 )
FILE_WRITE_ATTRIBUTES=     ( 256 )
FILE_ALL_ACCESS=           (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 1023)
FILE_GENERIC_READ=         (STANDARD_RIGHTS_READ | FILE_READ_DATA | FILE_READ_ATTRIBUTES | FILE_READ_EA | SYNCHRONIZE)
FILE_GENERIC_WRITE=        (STANDARD_RIGHTS_WRITE | FILE_WRITE_DATA | FILE_WRITE_ATTRIBUTES | FILE_WRITE_EA | FILE_APPEND_DATA | SYNCHRONIZE)
FILE_GENERIC_EXECUTE=      (STANDARD_RIGHTS_EXECUTE | FILE_READ_ATTRIBUTES | FILE_EXECUTE | SYNCHRONIZE)


SECURITY_NULL_SID_AUTHORITY = (0,0,0,0,0,0)
SECURITY_WORLD_SID_AUTHORITY = (0,0,0,0,0,1)
SECURITY_LOCAL_SID_AUTHORITY = (0,0,0,0,0,2)
SECURITY_CREATOR_SID_AUTHORITY = (0,0,0,0,0,3)
SECURITY_NON_UNIQUE_AUTHORITY = (0,0,0,0,0,4)
SECURITY_RESOURCE_MANAGER_AUTHORITY = (0,0,0,0,0,9)

SECURITY_NULL_RID                 = 0
SECURITY_WORLD_RID                = 0
SECURITY_LOCAL_RID                = 0X00000000

SECURITY_CREATOR_OWNER_RID        = 0
SECURITY_CREATOR_GROUP_RID        = 1

SECURITY_CREATOR_OWNER_SERVER_RID = 2
SECURITY_CREATOR_GROUP_SERVER_RID = 3
SECURITY_CREATOR_OWNER_RIGHTS_RID = 4

# NT well-known SIDs
SECURITY_NT_AUTHORITY = (0,0,0,0,0,5)

SECURITY_DIALUP_RID             = 1
SECURITY_NETWORK_RID            = 2
SECURITY_BATCH_RID              = 3
SECURITY_INTERACTIVE_RID        = 4
SECURITY_SERVICE_RID            = 6
SECURITY_ANONYMOUS_LOGON_RID    = 7
SECURITY_PROXY_RID              = 8
SECURITY_SERVER_LOGON_RID       = 9

SECURITY_LOGON_IDS_RID          = 5
SECURITY_LOGON_IDS_RID_COUNT    = 3

SECURITY_LOCAL_SYSTEM_RID       = 18

SECURITY_NT_NON_UNIQUE          = 21

SECURITY_BUILTIN_DOMAIN_RID     = 32

# well-known domain relative sub-authority values (RIDs)...
DOMAIN_USER_RID_ADMIN          = 500
DOMAIN_USER_RID_GUEST          = 501
DOMAIN_USER_RID_KRBTGT         = 502
DOMAIN_USER_RID_MAX            = 999

# well-known groups ...
DOMAIN_GROUP_RID_ADMINS        = 512
DOMAIN_GROUP_RID_USERS         = 513
DOMAIN_GROUP_RID_GUESTS        = 514
DOMAIN_GROUP_RID_COMPUTERS     = 515
DOMAIN_GROUP_RID_CONTROLLERS   = 516
DOMAIN_GROUP_RID_CERT_ADMINS   = 517
DOMAIN_GROUP_RID_SCHEMA_ADMINS = 518
DOMAIN_GROUP_RID_ENTERPRISE_ADMINS = 519
DOMAIN_GROUP_RID_POLICY_ADMINS = 520
DOMAIN_GROUP_RID_READONLY_CONTROLLERS = 521

# well-known aliases ...
DOMAIN_ALIAS_RID_ADMINS        = 544
DOMAIN_ALIAS_RID_USERS         = 545
DOMAIN_ALIAS_RID_GUESTS        = 546
DOMAIN_ALIAS_RID_POWER_USERS   = 547
DOMAIN_ALIAS_RID_ACCOUNT_OPS   = 548
DOMAIN_ALIAS_RID_SYSTEM_OPS    = 549
DOMAIN_ALIAS_RID_PRINT_OPS     = 550
DOMAIN_ALIAS_RID_BACKUP_OPS    = 551
DOMAIN_ALIAS_RID_REPLICATOR    = 552
DOMAIN_ALIAS_RID_RAS_SERVERS = 553
DOMAIN_ALIAS_RID_PREW2KCOMPACCESS = 554
DOMAIN_ALIAS_RID_REMOTE_DESKTOP_USERS = 555
DOMAIN_ALIAS_RID_NETWORK_CONFIGURATION_OPS = 556
DOMAIN_ALIAS_RID_INCOMING_FOREST_TRUST_BUILDERS = 557
DOMAIN_ALIAS_RID_MONITORING_USERS = 558
DOMAIN_ALIAS_RID_LOGGING_USERS = 559
DOMAIN_ALIAS_RID_AUTHORIZATIONACCESS = 560
DOMAIN_ALIAS_RID_TS_LICENSE_SERVERS = 561
DOMAIN_ALIAS_RID_DCOM_USERS = 562
DOMAIN_ALIAS_RID_IUSERS = 568
DOMAIN_ALIAS_RID_CRYPTO_OPERATORS = 569
DOMAIN_ALIAS_RID_CACHEABLE_PRINCIPALS_GROUP = 571
DOMAIN_ALIAS_RID_NON_CACHEABLE_PRINCIPALS_GROUP = 572
DOMAIN_ALIAS_RID_EVENT_LOG_READERS_GROUP = 573

SECURITY_MANDATORY_LABEL_AUTHORITY          = (0,0,0,0,0,16)
SECURITY_MANDATORY_UNTRUSTED_RID            = 0x00000000
SECURITY_MANDATORY_LOW_RID                  = 0x00001000
SECURITY_MANDATORY_MEDIUM_RID               = 0x00002000
SECURITY_MANDATORY_HIGH_RID                 = 0x00003000
SECURITY_MANDATORY_SYSTEM_RID               = 0x00004000
SECURITY_MANDATORY_PROTECTED_PROCESS_RID    = 0x00005000
SECURITY_MANDATORY_MAXIMUM_USER_RID = SECURITY_MANDATORY_SYSTEM_RID

SYSTEM_LUID             = (999, 0)
ANONYMOUS_LOGON_LUID    = (998, 0)
LOCALSERVICE_LUID       = (997, 0)
NETWORKSERVICE_LUID     = (996, 0)
IUSER_LUID              = (995, 0)

# Group attributes

SE_GROUP_MANDATORY              = 1
SE_GROUP_ENABLED_BY_DEFAULT     = 2
SE_GROUP_ENABLED                = 4
SE_GROUP_OWNER                  = 8
SE_GROUP_USE_FOR_DENY_ONLY      = 16
SE_GROUP_INTEGRITY              = 32
SE_GROUP_INTEGRITY_ENABLED      = 64
SE_GROUP_RESOURCE               = 536870912
SE_GROUP_LOGON_ID               = -1073741824


# User attributes
# (None yet defined.)

# ACE types
ACCESS_MIN_MS_ACE_TYPE = (0)
ACCESS_ALLOWED_ACE_TYPE = (0)
ACCESS_DENIED_ACE_TYPE = (1)
SYSTEM_AUDIT_ACE_TYPE = (2)
SYSTEM_ALARM_ACE_TYPE = (3)
ACCESS_MAX_MS_V2_ACE_TYPE = (3)
ACCESS_ALLOWED_COMPOUND_ACE_TYPE = (4)
ACCESS_MAX_MS_V3_ACE_TYPE = (4)
ACCESS_MIN_MS_OBJECT_ACE_TYPE = (5)
ACCESS_ALLOWED_OBJECT_ACE_TYPE = (5)
ACCESS_DENIED_OBJECT_ACE_TYPE = (6)
SYSTEM_AUDIT_OBJECT_ACE_TYPE = (7)
SYSTEM_ALARM_OBJECT_ACE_TYPE = (8)
ACCESS_MAX_MS_OBJECT_ACE_TYPE = (8)
ACCESS_MAX_MS_V4_ACE_TYPE = (8)
ACCESS_MAX_MS_ACE_TYPE = (8)
ACCESS_ALLOWED_CALLBACK_ACE_TYPE = 9
ACCESS_DENIED_CALLBACK_ACE_TYPE = 10
ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE = 11
ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE = 12
SYSTEM_AUDIT_CALLBACK_ACE_TYPE = 13
SYSTEM_ALARM_CALLBACK_ACE_TYPE = 14
SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE = 15
SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE = 16
SYSTEM_MANDATORY_LABEL_ACE_TYPE = 17
ACCESS_MAX_MS_V5_ACE_TYPE = 17

#  The following are the inherit flags that go into the AceFlags field
#  of an Ace header.

OBJECT_INHERIT_ACE               = 1
CONTAINER_INHERIT_ACE            = 2
NO_PROPAGATE_INHERIT_ACE         = 4
INHERIT_ONLY_ACE                 = 8
VALID_INHERIT_FLAGS              = 15


SUCCESSFUL_ACCESS_ACE_FLAG       = 64
FAILED_ACCESS_ACE_FLAG           = 128

SE_OWNER_DEFAULTED               = 1
SE_GROUP_DEFAULTED               = 2
SE_DACL_PRESENT                  = 4
SE_DACL_DEFAULTED                = 8
SE_SACL_PRESENT                  = 16
SE_SACL_DEFAULTED                = 32
SE_SELF_RELATIVE                 = 32768


SE_PRIVILEGE_ENABLED_BY_DEFAULT = 1
SE_PRIVILEGE_ENABLED            = 2
SE_PRIVILEGE_USED_FOR_ACCESS    = -2147483648

PRIVILEGE_SET_ALL_NECESSARY    = 1

#               NT Defined Privileges

SE_CREATE_TOKEN_NAME              = "SeCreateTokenPrivilege"
SE_ASSIGNPRIMARYTOKEN_NAME        = "SeAssignPrimaryTokenPrivilege"
SE_LOCK_MEMORY_NAME               = "SeLockMemoryPrivilege"
SE_INCREASE_QUOTA_NAME            = "SeIncreaseQuotaPrivilege"
SE_UNSOLICITED_INPUT_NAME         = "SeUnsolicitedInputPrivilege"
SE_MACHINE_ACCOUNT_NAME           = "SeMachineAccountPrivilege"
SE_TCB_NAME                       = "SeTcbPrivilege"
SE_SECURITY_NAME                  = "SeSecurityPrivilege"
SE_TAKE_OWNERSHIP_NAME            = "SeTakeOwnershipPrivilege"
SE_LOAD_DRIVER_NAME               = "SeLoadDriverPrivilege"
SE_SYSTEM_PROFILE_NAME            = "SeSystemProfilePrivilege"
SE_SYSTEMTIME_NAME                = "SeSystemtimePrivilege"
SE_PROF_SINGLE_PROCESS_NAME       = "SeProfileSingleProcessPrivilege"
SE_INC_BASE_PRIORITY_NAME         = "SeIncreaseBasePriorityPrivilege"
SE_CREATE_PAGEFILE_NAME           = "SeCreatePagefilePrivilege"
SE_CREATE_PERMANENT_NAME          = "SeCreatePermanentPrivilege"
SE_BACKUP_NAME                    = "SeBackupPrivilege"
SE_RESTORE_NAME                   = "SeRestorePrivilege"
SE_SHUTDOWN_NAME                  = "SeShutdownPrivilege"
SE_DEBUG_NAME                     = "SeDebugPrivilege"
SE_AUDIT_NAME                     = "SeAuditPrivilege"
SE_SYSTEM_ENVIRONMENT_NAME        = "SeSystemEnvironmentPrivilege"
SE_CHANGE_NOTIFY_NAME             = "SeChangeNotifyPrivilege"
SE_REMOTE_SHUTDOWN_NAME           = "SeRemoteShutdownPrivilege"


# Enum SECURITY_IMPERSONATION_LEVEL:
SecurityAnonymous = 0
SecurityIdentification = 1
SecurityImpersonation = 2
SecurityDelegation = 3

SECURITY_MAX_IMPERSONATION_LEVEL = SecurityDelegation

DEFAULT_IMPERSONATION_LEVEL = SecurityImpersonation

TOKEN_ASSIGN_PRIMARY    = 1
TOKEN_DUPLICATE         = 2
TOKEN_IMPERSONATE       = 4
TOKEN_QUERY             = 8
TOKEN_QUERY_SOURCE      = 16
TOKEN_ADJUST_PRIVILEGES = 32
TOKEN_ADJUST_GROUPS     = 64
TOKEN_ADJUST_DEFAULT    = 128

TOKEN_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED  |\
                          TOKEN_ASSIGN_PRIMARY      |\
                          TOKEN_DUPLICATE           |\
                          TOKEN_IMPERSONATE         |\
                          TOKEN_QUERY               |\
                          TOKEN_QUERY_SOURCE        |\
                          TOKEN_ADJUST_PRIVILEGES   |\
                          TOKEN_ADJUST_GROUPS       |\
                          TOKEN_ADJUST_DEFAULT)


TOKEN_READ       = (STANDARD_RIGHTS_READ      |\
                          TOKEN_QUERY)


TOKEN_WRITE      = (STANDARD_RIGHTS_WRITE     |\
                          TOKEN_ADJUST_PRIVILEGES   |\
                          TOKEN_ADJUST_GROUPS       |\
                          TOKEN_ADJUST_DEFAULT)

TOKEN_EXECUTE    = (STANDARD_RIGHTS_EXECUTE)

SidTypeUser = 1
SidTypeGroup = 2
SidTypeDomain =3
SidTypeAlias = 4
SidTypeWellKnownGroup = 5
SidTypeDeletedAccount = 6
SidTypeInvalid = 7
SidTypeUnknown = 8
SidTypeComputer = 9
SidTypeLabel = 10

# Token types
TokenPrimary = 1
TokenImpersonation = 2

# TOKEN_INFORMATION_CLASS, used with Get/SetTokenInformation
TokenUser = 1
TokenGroups = 2
TokenPrivileges = 3
TokenOwner = 4
TokenPrimaryGroup = 5
TokenDefaultDacl = 6
TokenSource = 7
TokenType = 8
TokenImpersonationLevel = 9
TokenStatistics = 10
TokenRestrictedSids = 11
TokenSessionId = 12
TokenGroupsAndPrivileges = 13
TokenSessionReference = 14
TokenSandBoxInert = 15
TokenAuditPolicy = 16
TokenOrigin = 17
TokenElevationType = 18
TokenLinkedToken = 19
TokenElevation = 20
TokenHasRestrictions = 21
TokenAccessInformation = 22
TokenVirtualizationAllowed = 23
TokenVirtualizationEnabled = 24
TokenIntegrityLevel = 25
TokenUIAccess = 26
TokenMandatoryPolicy = 27
TokenLogonSid = 28

# DirectoryService related constants.
# Generated by h2py from NtDsAPI.h
DS_BEHAVIOR_WIN2000 = 0
DS_BEHAVIOR_WIN2003_WITH_MIXED_DOMAINS = 1
DS_BEHAVIOR_WIN2003 = 2
DS_SYNCED_EVENT_NAME = "NTDSInitialSyncsCompleted"
ACTRL_DS_OPEN = 0x00000000
ACTRL_DS_CREATE_CHILD = 0x00000001
ACTRL_DS_DELETE_CHILD = 0x00000002
ACTRL_DS_LIST = 0x00000004
ACTRL_DS_SELF = 0x00000008
ACTRL_DS_READ_PROP = 0x00000010
ACTRL_DS_WRITE_PROP = 0x00000020
ACTRL_DS_DELETE_TREE = 0x00000040
ACTRL_DS_LIST_OBJECT = 0x00000080
ACTRL_DS_CONTROL_ACCESS = 0x00000100
NTDSAPI_BIND_ALLOW_DELEGATION = (0x00000001)
DS_REPSYNC_ASYNCHRONOUS_OPERATION = 0x00000001
DS_REPSYNC_WRITEABLE = 0x00000002
DS_REPSYNC_PERIODIC = 0x00000004
DS_REPSYNC_INTERSITE_MESSAGING = 0x00000008
DS_REPSYNC_ALL_SOURCES = 0x00000010
DS_REPSYNC_FULL = 0x00000020
DS_REPSYNC_URGENT = 0x00000040
DS_REPSYNC_NO_DISCARD = 0x00000080
DS_REPSYNC_FORCE = 0x00000100
DS_REPSYNC_ADD_REFERENCE = 0x00000200
DS_REPSYNC_NEVER_COMPLETED = 0x00000400
DS_REPSYNC_TWO_WAY = 0x00000800
DS_REPSYNC_NEVER_NOTIFY = 0x00001000
DS_REPSYNC_INITIAL = 0x00002000
DS_REPSYNC_USE_COMPRESSION = 0x00004000
DS_REPSYNC_ABANDONED = 0x00008000
DS_REPSYNC_INITIAL_IN_PROGRESS = 0x00010000
DS_REPSYNC_PARTIAL_ATTRIBUTE_SET = 0x00020000
DS_REPSYNC_REQUEUE = 0x00040000
DS_REPSYNC_NOTIFICATION = 0x00080000
DS_REPSYNC_ASYNCHRONOUS_REPLICA = 0x00100000
DS_REPSYNC_CRITICAL = 0x00200000
DS_REPSYNC_FULL_IN_PROGRESS = 0x00400000
DS_REPSYNC_PREEMPTED = 0x00800000
DS_REPADD_ASYNCHRONOUS_OPERATION = 0x00000001
DS_REPADD_WRITEABLE = 0x00000002
DS_REPADD_INITIAL = 0x00000004
DS_REPADD_PERIODIC = 0x00000008
DS_REPADD_INTERSITE_MESSAGING = 0x00000010
DS_REPADD_ASYNCHRONOUS_REPLICA = 0x00000020
DS_REPADD_DISABLE_NOTIFICATION = 0x00000040
DS_REPADD_DISABLE_PERIODIC = 0x00000080
DS_REPADD_USE_COMPRESSION = 0x00000100
DS_REPADD_NEVER_NOTIFY = 0x00000200
DS_REPADD_TWO_WAY = 0x00000400
DS_REPADD_CRITICAL = 0x00000800
DS_REPDEL_ASYNCHRONOUS_OPERATION = 0x00000001
DS_REPDEL_WRITEABLE = 0x00000002
DS_REPDEL_INTERSITE_MESSAGING = 0x00000004
DS_REPDEL_IGNORE_ERRORS = 0x00000008
DS_REPDEL_LOCAL_ONLY = 0x00000010
DS_REPDEL_NO_SOURCE = 0x00000020
DS_REPDEL_REF_OK = 0x00000040
DS_REPMOD_ASYNCHRONOUS_OPERATION = 0x00000001
DS_REPMOD_WRITEABLE = 0x00000002
DS_REPMOD_UPDATE_FLAGS = 0x00000001
DS_REPMOD_UPDATE_ADDRESS = 0x00000002
DS_REPMOD_UPDATE_SCHEDULE = 0x00000004
DS_REPMOD_UPDATE_RESULT = 0x00000008
DS_REPMOD_UPDATE_TRANSPORT = 0x00000010
DS_REPUPD_ASYNCHRONOUS_OPERATION = 0x00000001
DS_REPUPD_WRITEABLE = 0x00000002
DS_REPUPD_ADD_REFERENCE = 0x00000004
DS_REPUPD_DELETE_REFERENCE = 0x00000008
DS_INSTANCETYPE_IS_NC_HEAD = 0x00000001
DS_INSTANCETYPE_NC_IS_WRITEABLE = 0x00000004
DS_INSTANCETYPE_NC_COMING = 0x00000010
DS_INSTANCETYPE_NC_GOING = 0x00000020
NTDSDSA_OPT_IS_GC = ( 1 << 0 )
NTDSDSA_OPT_DISABLE_INBOUND_REPL = ( 1 << 1 )
NTDSDSA_OPT_DISABLE_OUTBOUND_REPL = ( 1 << 2 )
NTDSDSA_OPT_DISABLE_NTDSCONN_XLATE = ( 1 << 3 )
NTDSCONN_OPT_IS_GENERATED = ( 1 << 0 )
NTDSCONN_OPT_TWOWAY_SYNC = ( 1 << 1 )
NTDSCONN_OPT_OVERRIDE_NOTIFY_DEFAULT = (1 << 2 )
NTDSCONN_OPT_USE_NOTIFY = (1 << 3)
NTDSCONN_OPT_DISABLE_INTERSITE_COMPRESSION = (1 << 4)
NTDSCONN_OPT_USER_OWNED_SCHEDULE = (1 << 5)
NTDSCONN_KCC_NO_REASON = ( 0 )
NTDSCONN_KCC_GC_TOPOLOGY = ( 1 << 0 )
NTDSCONN_KCC_RING_TOPOLOGY = ( 1 << 1 )
NTDSCONN_KCC_MINIMIZE_HOPS_TOPOLOGY = ( 1 << 2 )
NTDSCONN_KCC_STALE_SERVERS_TOPOLOGY = ( 1 << 3 )
NTDSCONN_KCC_OSCILLATING_CONNECTION_TOPOLOGY = ( 1 << 4 )
NTDSCONN_KCC_INTERSITE_GC_TOPOLOGY = (1 << 5)
NTDSCONN_KCC_INTERSITE_TOPOLOGY = (1 << 6)
NTDSCONN_KCC_SERVER_FAILOVER_TOPOLOGY = (1 << 7)
NTDSCONN_KCC_SITE_FAILOVER_TOPOLOGY = (1 << 8)
NTDSCONN_KCC_REDUNDANT_SERVER_TOPOLOGY = (1 << 9)
FRSCONN_PRIORITY_MASK = 0x70000000
FRSCONN_MAX_PRIORITY = 0x8
NTDSCONN_OPT_IGNORE_SCHEDULE_MASK = (-2147483648)

NTDSSETTINGS_OPT_IS_AUTO_TOPOLOGY_DISABLED = ( 1 << 0 )
NTDSSETTINGS_OPT_IS_TOPL_CLEANUP_DISABLED = ( 1 << 1 )
NTDSSETTINGS_OPT_IS_TOPL_MIN_HOPS_DISABLED = ( 1 << 2 )
NTDSSETTINGS_OPT_IS_TOPL_DETECT_STALE_DISABLED = ( 1 << 3 )
NTDSSETTINGS_OPT_IS_INTER_SITE_AUTO_TOPOLOGY_DISABLED = ( 1 << 4 )
NTDSSETTINGS_OPT_IS_GROUP_CACHING_ENABLED = ( 1 << 5 )
NTDSSETTINGS_OPT_FORCE_KCC_WHISTLER_BEHAVIOR = ( 1 << 6 )
NTDSSETTINGS_OPT_FORCE_KCC_W2K_ELECTION = ( 1 << 7 )
NTDSSETTINGS_OPT_IS_RAND_BH_SELECTION_DISABLED = ( 1 << 8 )
NTDSSETTINGS_OPT_IS_SCHEDULE_HASHING_ENABLED = ( 1 << 9 )
NTDSSETTINGS_OPT_IS_REDUNDANT_SERVER_TOPOLOGY_ENABLED = ( 1 << 10 )
NTDSSETTINGS_DEFAULT_SERVER_REDUNDANCY = 2
NTDSTRANSPORT_OPT_IGNORE_SCHEDULES = ( 1 << 0 )
NTDSTRANSPORT_OPT_BRIDGES_REQUIRED = (1 << 1 )
NTDSSITECONN_OPT_USE_NOTIFY = ( 1 << 0 )
NTDSSITECONN_OPT_TWOWAY_SYNC = ( 1 << 1 )
NTDSSITECONN_OPT_DISABLE_COMPRESSION = ( 1 << 2 )
NTDSSITELINK_OPT_USE_NOTIFY = ( 1 << 0 )
NTDSSITELINK_OPT_TWOWAY_SYNC = ( 1 << 1 )
NTDSSITELINK_OPT_DISABLE_COMPRESSION = ( 1 << 2 )
GUID_USERS_CONTAINER_A = "a9d1ca15768811d1aded00c04fd8d5cd"
GUID_COMPUTRS_CONTAINER_A = "aa312825768811d1aded00c04fd8d5cd"
GUID_SYSTEMS_CONTAINER_A = "ab1d30f3768811d1aded00c04fd8d5cd"
GUID_DOMAIN_CONTROLLERS_CONTAINER_A = "a361b2ffffd211d1aa4b00c04fd7d83a"
GUID_INFRASTRUCTURE_CONTAINER_A = "2fbac1870ade11d297c400c04fd8d5cd"
GUID_DELETED_OBJECTS_CONTAINER_A = "18e2ea80684f11d2b9aa00c04f79f805"
GUID_LOSTANDFOUND_CONTAINER_A = "ab8153b7768811d1aded00c04fd8d5cd"
GUID_FOREIGNSECURITYPRINCIPALS_CONTAINER_A = "22b70c67d56e4efb91e9300fca3dc1aa"
GUID_PROGRAM_DATA_CONTAINER_A = "09460c08ae1e4a4ea0f64aee7daa1e5a"
GUID_MICROSOFT_PROGRAM_DATA_CONTAINER_A = "f4be92a4c777485e878e9421d53087db"
GUID_NTDS_QUOTAS_CONTAINER_A = "6227f0af1fc2410d8e3bb10615bb5b0f"
GUID_USERS_CONTAINER_BYTE = "\xa9\xd1\xca\x15\x76\x88\x11\xd1\xad\xed\x00\xc0\x4f\xd8\xd5\xcd"
GUID_COMPUTRS_CONTAINER_BYTE = "\xaa\x31\x28\x25\x76\x88\x11\xd1\xad\xed\x00\xc0\x4f\xd8\xd5\xcd"
GUID_SYSTEMS_CONTAINER_BYTE = "\xab\x1d\x30\xf3\x76\x88\x11\xd1\xad\xed\x00\xc0\x4f\xd8\xd5\xcd"
GUID_DOMAIN_CONTROLLERS_CONTAINER_BYTE = "\xa3\x61\xb2\xff\xff\xd2\x11\xd1\xaa\x4b\x00\xc0\x4f\xd7\xd8\x3a"
GUID_INFRASTRUCTURE_CONTAINER_BYTE = "\x2f\xba\xc1\x87\x0a\xde\x11\xd2\x97\xc4\x00\xc0\x4f\xd8\xd5\xcd"
GUID_DELETED_OBJECTS_CONTAINER_BYTE = "\x18\xe2\xea\x80\x68\x4f\x11\xd2\xb9\xaa\x00\xc0\x4f\x79\xf8\x05"
GUID_LOSTANDFOUND_CONTAINER_BYTE = "\xab\x81\x53\xb7\x76\x88\x11\xd1\xad\xed\x00\xc0\x4f\xd8\xd5\xcd"
GUID_FOREIGNSECURITYPRINCIPALS_CONTAINER_BYTE = "\x22\xb7\x0c\x67\xd5\x6e\x4e\xfb\x91\xe9\x30\x0f\xca\x3d\xc1\xaa"
GUID_PROGRAM_DATA_CONTAINER_BYTE = "\x09\x46\x0c\x08\xae\x1e\x4a\x4e\xa0\xf6\x4a\xee\x7d\xaa\x1e\x5a"
GUID_MICROSOFT_PROGRAM_DATA_CONTAINER_BYTE = "\xf4\xbe\x92\xa4\xc7\x77\x48\x5e\x87\x8e\x94\x21\xd5\x30\x87\xdb"
GUID_NTDS_QUOTAS_CONTAINER_BYTE = "\x62\x27\xf0\xaf\x1f\xc2\x41\x0d\x8e\x3b\xb1\x06\x15\xbb\x5b\x0f"
DS_REPSYNCALL_NO_OPTIONS = 0x00000000
DS_REPSYNCALL_ABORT_IF_SERVER_UNAVAILABLE = 0x00000001
DS_REPSYNCALL_SYNC_ADJACENT_SERVERS_ONLY = 0x00000002
DS_REPSYNCALL_ID_SERVERS_BY_DN = 0x00000004
DS_REPSYNCALL_DO_NOT_SYNC = 0x00000008
DS_REPSYNCALL_SKIP_INITIAL_CHECK = 0x00000010
DS_REPSYNCALL_PUSH_CHANGES_OUTWARD = 0x00000020
DS_REPSYNCALL_CROSS_SITE_BOUNDARIES = 0x00000040
DS_LIST_DSA_OBJECT_FOR_SERVER = 0
DS_LIST_DNS_HOST_NAME_FOR_SERVER = 1
DS_LIST_ACCOUNT_OBJECT_FOR_SERVER = 2
DS_ROLE_SCHEMA_OWNER = 0
DS_ROLE_DOMAIN_OWNER = 1
DS_ROLE_PDC_OWNER = 2
DS_ROLE_RID_OWNER = 3
DS_ROLE_INFRASTRUCTURE_OWNER = 4
DS_SCHEMA_GUID_NOT_FOUND = 0
DS_SCHEMA_GUID_ATTR = 1
DS_SCHEMA_GUID_ATTR_SET = 2
DS_SCHEMA_GUID_CLASS = 3
DS_SCHEMA_GUID_CONTROL_RIGHT = 4
DS_KCC_FLAG_ASYNC_OP = (1 << 0)
DS_KCC_FLAG_DAMPED = (1 << 1)
DS_EXIST_ADVISORY_MODE = (0x1)
DS_REPL_INFO_FLAG_IMPROVE_LINKED_ATTRS = (0x00000001)
DS_REPL_NBR_WRITEABLE = (0x00000010)
DS_REPL_NBR_SYNC_ON_STARTUP = (0x00000020)
DS_REPL_NBR_DO_SCHEDULED_SYNCS = (0x00000040)
DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT = (0x00000080)
DS_REPL_NBR_TWO_WAY_SYNC = (0x00000200)
DS_REPL_NBR_RETURN_OBJECT_PARENTS = (0x00000800)
DS_REPL_NBR_FULL_SYNC_IN_PROGRESS = (0x00010000)
DS_REPL_NBR_FULL_SYNC_NEXT_PACKET = (0x00020000)
DS_REPL_NBR_NEVER_SYNCED = (0x00200000)
DS_REPL_NBR_PREEMPTED = (0x01000000)
DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS = (0x04000000)
DS_REPL_NBR_DISABLE_SCHEDULED_SYNC = (0x08000000)
DS_REPL_NBR_COMPRESS_CHANGES = (0x10000000)
DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS = (0x20000000)
DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET = (0x40000000)
DS_REPL_NBR_MODIFIABLE_MASK = \
        ( \
        DS_REPL_NBR_SYNC_ON_STARTUP | \
        DS_REPL_NBR_DO_SCHEDULED_SYNCS | \
        DS_REPL_NBR_TWO_WAY_SYNC | \
        DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS | \
        DS_REPL_NBR_DISABLE_SCHEDULED_SYNC | \
        DS_REPL_NBR_COMPRESS_CHANGES | \
        DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS \
        )

# from enum DS_NAME_FORMAT
DS_UNKNOWN_NAME = 0
DS_FQDN_1779_NAME = 1
DS_NT4_ACCOUNT_NAME = 2
DS_DISPLAY_NAME = 3
DS_UNIQUE_ID_NAME = 6
DS_CANONICAL_NAME = 7
DS_USER_PRINCIPAL_NAME = 8
DS_CANONICAL_NAME_EX = 9
DS_SERVICE_PRINCIPAL_NAME = 10
DS_SID_OR_SID_HISTORY_NAME = 11
DS_DNS_DOMAIN_NAME = 12

DS_DOMAIN_SIMPLE_NAME = DS_USER_PRINCIPAL_NAME
DS_ENTERPRISE_SIMPLE_NAME = DS_USER_PRINCIPAL_NAME

# from enum DS_NAME_FLAGS
DS_NAME_NO_FLAGS = 0x0
DS_NAME_FLAG_SYNTACTICAL_ONLY = 0x1
DS_NAME_FLAG_EVAL_AT_DC = 0x2
DS_NAME_FLAG_GCVERIFY = 0x4
DS_NAME_FLAG_TRUST_REFERRAL = 0x8

# from enum DS_NAME_ERROR
DS_NAME_NO_ERROR = 0
DS_NAME_ERROR_RESOLVING = 1
DS_NAME_ERROR_NOT_FOUND = 2
DS_NAME_ERROR_NOT_UNIQUE = 3
DS_NAME_ERROR_NO_MAPPING = 4
DS_NAME_ERROR_DOMAIN_ONLY = 5
DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING = 6
DS_NAME_ERROR_TRUST_REFERRAL = 7


# from enum DS_SPN_NAME_TYPE
DS_SPN_DNS_HOST = 0
DS_SPN_DN_HOST = 1
DS_SPN_NB_HOST = 2
DS_SPN_DOMAIN = 3
DS_SPN_NB_DOMAIN = 4
DS_SPN_SERVICE = 5

# from enum DS_SPN_WRITE_OP
DS_SPN_ADD_SPN_OP = 0
DS_SPN_REPLACE_SPN_OP = 1
DS_SPN_DELETE_SPN_OP = 2  

# Generated by h2py from DsGetDC.h
DS_FORCE_REDISCOVERY = 0x00000001
DS_DIRECTORY_SERVICE_REQUIRED = 0x00000010
DS_DIRECTORY_SERVICE_PREFERRED = 0x00000020
DS_GC_SERVER_REQUIRED = 0x00000040
DS_PDC_REQUIRED = 0x00000080
DS_BACKGROUND_ONLY = 0x00000100
DS_IP_REQUIRED = 0x00000200
DS_KDC_REQUIRED = 0x00000400
DS_TIMESERV_REQUIRED = 0x00000800
DS_WRITABLE_REQUIRED = 0x00001000
DS_GOOD_TIMESERV_PREFERRED = 0x00002000
DS_AVOID_SELF = 0x00004000
DS_ONLY_LDAP_NEEDED = 0x00008000
DS_IS_FLAT_NAME = 0x00010000
DS_IS_DNS_NAME = 0x00020000
DS_RETURN_DNS_NAME = 0x40000000
DS_RETURN_FLAT_NAME = (-2147483648)
DSGETDC_VALID_FLAGS = ( \
            DS_FORCE_REDISCOVERY | \
            DS_DIRECTORY_SERVICE_REQUIRED | \
            DS_DIRECTORY_SERVICE_PREFERRED | \
            DS_GC_SERVER_REQUIRED | \
            DS_PDC_REQUIRED | \
            DS_BACKGROUND_ONLY | \
            DS_IP_REQUIRED | \
            DS_KDC_REQUIRED | \
            DS_TIMESERV_REQUIRED | \
            DS_WRITABLE_REQUIRED | \
            DS_GOOD_TIMESERV_PREFERRED | \
            DS_AVOID_SELF | \
            DS_ONLY_LDAP_NEEDED | \
            DS_IS_FLAT_NAME | \
            DS_IS_DNS_NAME | \
            DS_RETURN_FLAT_NAME  | \
            DS_RETURN_DNS_NAME )
DS_INET_ADDRESS = 1
DS_NETBIOS_ADDRESS = 2
DS_PDC_FLAG = 0x00000001
DS_GC_FLAG = 0x00000004
DS_LDAP_FLAG = 0x00000008
DS_DS_FLAG = 0x00000010
DS_KDC_FLAG = 0x00000020
DS_TIMESERV_FLAG = 0x00000040
DS_CLOSEST_FLAG = 0x00000080
DS_WRITABLE_FLAG = 0x00000100
DS_GOOD_TIMESERV_FLAG = 0x00000200
DS_NDNC_FLAG = 0x00000400
DS_PING_FLAGS = 0x0000FFFF
DS_DNS_CONTROLLER_FLAG = 0x20000000
DS_DNS_DOMAIN_FLAG = 0x40000000
DS_DNS_FOREST_FLAG = (-2147483648)
DS_DOMAIN_IN_FOREST = 0x0001
DS_DOMAIN_DIRECT_OUTBOUND = 0x0002
DS_DOMAIN_TREE_ROOT = 0x0004
DS_DOMAIN_PRIMARY = 0x0008
DS_DOMAIN_NATIVE_MODE = 0x0010
DS_DOMAIN_DIRECT_INBOUND = 0x0020
DS_DOMAIN_VALID_FLAGS = (         \
            DS_DOMAIN_IN_FOREST       | \
            DS_DOMAIN_DIRECT_OUTBOUND | \
            DS_DOMAIN_TREE_ROOT       | \
            DS_DOMAIN_PRIMARY         | \
            DS_DOMAIN_NATIVE_MODE     | \
            DS_DOMAIN_DIRECT_INBOUND )
DS_GFTI_UPDATE_TDO = 0x1
DS_GFTI_VALID_FLAGS = 0x1
DS_ONLY_DO_SITE_NAME = 0x01
DS_NOTIFY_AFTER_SITE_RECORDS = 0x02
DS_OPEN_VALID_OPTION_FLAGS = ( DS_ONLY_DO_SITE_NAME | DS_NOTIFY_AFTER_SITE_RECORDS )
DS_OPEN_VALID_FLAGS = (       \
            DS_FORCE_REDISCOVERY  | \
            DS_ONLY_LDAP_NEEDED   | \
            DS_KDC_REQUIRED       | \
            DS_PDC_REQUIRED       | \
            DS_GC_SERVER_REQUIRED | \
            DS_WRITABLE_REQUIRED )

## from aclui.h
# SI_OBJECT_INFO.dwFlags
SI_EDIT_PERMS = 0x00000000
SI_EDIT_OWNER = 0x00000001
SI_EDIT_AUDITS = 0x00000002
SI_CONTAINER = 0x00000004
SI_READONLY = 0x00000008
SI_ADVANCED = 0x00000010
SI_RESET = 0x00000020
SI_OWNER_READONLY = 0x00000040
SI_EDIT_PROPERTIES = 0x00000080
SI_OWNER_RECURSE = 0x00000100
SI_NO_ACL_PROTECT = 0x00000200
SI_NO_TREE_APPLY = 0x00000400
SI_PAGE_TITLE = 0x00000800
SI_SERVER_IS_DC = 0x00001000
SI_RESET_DACL_TREE = 0x00004000
SI_RESET_SACL_TREE = 0x00008000
SI_OBJECT_GUID = 0x00010000
SI_EDIT_EFFECTIVE = 0x00020000
SI_RESET_DACL = 0x00040000
SI_RESET_SACL = 0x00080000
SI_RESET_OWNER = 0x00100000
SI_NO_ADDITIONAL_PERMISSION = 0x00200000
SI_MAY_WRITE = 0x10000000
SI_EDIT_ALL = (SI_EDIT_PERMS | SI_EDIT_OWNER | SI_EDIT_AUDITS)
SI_AUDITS_ELEVATION_REQUIRED = 0x02000000
SI_VIEW_ONLY = 0x00400000
SI_OWNER_ELEVATION_REQUIRED = 0x04000000
SI_PERMS_ELEVATION_REQUIRED = 0x01000000

# SI_ACCESS.dwFlags
SI_ACCESS_SPECIFIC = 0x00010000
SI_ACCESS_GENERAL = 0x00020000
SI_ACCESS_CONTAINER = 0x00040000
SI_ACCESS_PROPERTY = 0x00080000

# SI_PAGE_TYPE enum
SI_PAGE_PERM = 0
SI_PAGE_ADVPERM = 1
SI_PAGE_AUDIT = 2
SI_PAGE_OWNER = 3
SI_PAGE_EFFECTIVE =4

CFSTR_ACLUI_SID_INFO_LIST = "CFSTR_ACLUI_SID_INFO_LIST"
PSPCB_SI_INITDIALOG = 1025 ## WM_USER+1
