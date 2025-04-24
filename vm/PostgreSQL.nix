{
  lib,
  pkgs,
  ...
}: {
  config = {
    services = {
      getty.autologinUser = "root";
      postgresql = {
        enable = true;
        settings.listen_addresses = lib.mkForce "*";

        ensureUsers = [
          {
            name = "user";
            ensureClauses = {
              login = true;
              # password = "password";
              superuser = true;
            };
          }
        ];

        ensureDatabases = ["post"];

        authentication = ''
          host all all 0.0.0.0/0 trust

          host all all 0.0.0.0/0 scram-sha-256

          local all all trust

          host all all 127.0.0.1/32 trust

          host all all ::1/128 trust
        '';
      };
      # nginx = {
      #   enable = true;
      # };
    };

    networking.firewall.allowedTCPPorts = [5432];

    virtualisation.forwardPorts = [
      {
        from = "host";
        guest.port = 5432;
        host.port = 5432;
      }
    ];

    system.stateVersion = "24.11";
  };
}
