{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";

    nixpkgs.url = "github:NixOS/nixpkgs/24.11";
  };

  outputs = {
    flake-utils,
    nixpkgs,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages."${system}";

        base = {modulesPath, ...}: {
          imports = ["${modulesPath}/virtualisation/qemu-vm.nix"];

          virtualisation = {
            graphics = false;

            host = {inherit pkgs;};
          };
        };

        machine = nixpkgs.lib.nixosSystem {
          system = system;
          modules = [base ./PostgreSQL.nix];
        };

        program = pkgs.writeShellScript "run-vm.sh" ''
          export NIX_DISK_IMAGE=$(mktemp -u -t nixos.qcow2.XXXXX)

          ${machine.config.system.build.vm}/bin/run-nixos-vm
        '';
      in {
        packages = {inherit machine;};

        apps.default = {
          type = "app";

          program = "${program}";
        };
      }
    );
}
