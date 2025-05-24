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
        pythonPackages = pkgs.python311Packages;
        cp = "cp311";

        lightfm = let
          pname = "lightfm";
          version = "1.17";
        in
          pythonPackages.buildPythonPackage {
            inherit pname version;
            src = pkgs.fetchPypi {
              inherit pname version;
              sha256 = "K3etoYLM12io12Q6s8/Ni26FXbCQh/fMcym9YzFml6g=";
            };
            doCheck = false;
          };

        # pandas-stubs = let
        #   pname = "pandas_stubs";
        #   version = "2.2.3.250308";
        # in
        #   pythonPackages.buildPythonPackage {
        #     inherit pname version;
        #     src = pkgs.fetchPypi {
        #       inherit pname version;
        #       sha256 = "Om6drxYfALhcg3cu09XP+VIgKPB6lIF0csB7kfRnEP0=";
        #     };
        #     doCheck = false;
        #     format = "pyproject";
        #     nativeBuildInputs = with pythonPackages; [
        #       poetry-core
        #       numpy
        #       pandas
        #       # scikit-learn
        #       # scipy
        #       # statsmodels
        #     ];
        #     # ++ [patsy];
        #   };

        patsy = let
          pname = "patsy";
          version = "1.0.1";
        in
          pythonPackages.buildPythonPackage {
            inherit pname version;
            src = pkgs.fetchPypi {
              inherit pname version;
              sha256 = "54apOR7sgYwFTjWbc3u85pLwUa7kxmH0FBzIj7RZwMQ=";
            };
            doCheck = false;
          };

        # jupyterlab-vim = let
        #   pname = "jupyterlab_vim";
        #   version = "4.1.4";
        # in
        #   pythonPackages.buildPythonPackage {
        #     inherit pname version;
        #     src = pkgs.fetchPypi {
        #       inherit pname version;
        #       sha256 = "sha256-q/KJGq+zLwy5StmDIa5+vL4Mq+Uj042A1WnApQuFIlo=";
        #     };
        #     doCheck = false;
        #     format = "pyproject";
        #     nativeBuildInputs = with pythonPackages; [
        #       hatchling
        #     ];
        #   };
        #
        # hatchling = let
        #   pname = "hatchling";
        #   version = "1.27.0";
        # in
        #   pythonPackages.buildPythonPackage {
        #     inherit pname version;
        #     src = pkgs.fetchPypi {
        #       inherit pname version;
        #       sha256 = "sha256-lxwpbZgZq7OBERL8UsepdRyNOBiY82Uzuxb5eR6UH9Y=";
        #     };
        #     doCheck = false;
        #     format = "pyproject";
        #     nativeBuildInputs = with pythonPackages; [
        #       hatchling
        #     ];
        #   };

        category-encoders = let
          pname = "category_encoders";
          version = "2.8.1";
        in
          pythonPackages.buildPythonPackage {
            inherit pname version;
            src = pkgs.fetchPypi {
              inherit pname version;
              sha256 = "V6+KI73jz2Iu5+F8EVRwEXleTTN4OdQMvRbDa2cpGzM=";
            };
            doCheck = false;
            format = "pyproject";
            nativeBuildInputs = with pythonPackages;
              [
                poetry-core
                numpy
                pandas
                scikit-learn
                scipy
                statsmodels
              ]
              ++ [patsy];
          };

        implicit = let
          pname = "implicit";
          version = "0.7.2";
          format = "wheel";
        in
          pythonPackages.buildPythonPackage {
            inherit pname version format;
            src = pkgs.fetchPypi {
              inherit pname version format;
              sha256 = "HxYcl9RVtxDm1ok36H7NIv8hK8biLcV3SLdsat5Cq8I=";
              dist = "${cp}";
              python = "${cp}";
              abi = "${cp}";
              platform = "manylinux2014_x86_64";
            };
          };
      in let
        pythonEnv = pkgs.python311.withPackages (ps:
          with ps; [
            pytest
            fastapi
            uvicorn
            psycopg2-binary
            sqlalchemy

            pandas
            statsmodels
            # pandas-stubs
            requests
            pydantic
            scikit-learn
            matplotlib
            xgboost
            loguru
            lightfm
            category-encoders
            implicit
            numpy
            seaborn
            ipykernel
            # jupyterlab-vim
            jupyter
            tqdm
          ]);
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            pkgs.jq
          ];

          shellHook = ''
            # явно экспортируем PYTHONPATH
            export PYTHONPATH="${pythonEnv}:$PYTHONPATH:${pythonEnv}/${pythonEnv.sitePackages}"
          '';
        };
      }
    );
}
