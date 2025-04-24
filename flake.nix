{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {inherit system;};
        pythonEnv = pkgs.python312.withPackages (ps:
          with ps; [
            pytest
            fastapi
            uvicorn
            psycopg2
            sqlalchemy
          ]);
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            pythonEnv
          ];

          shellHook = ''
            # явно экспортируем PYTHONPATH
            export PYTHONPATH="${pythonEnv}:$PYTHONPATH:${pythonEnv}/${pythonEnv.sitePackages}"
            exec zsh
          '';
        };
      }
    );
}
