This repository contains sources for RPMs that are used
to build Software Collections for CentOS by SCLo SIG.

This branch is for libtidy-devel, dependency of php-tidy
This package only build the static library, only for EL-7

    build -bs *spec --define "dist .el7"
    cbs add-pkg    sclo7-sclo-php70-sclo-candidate --owner=sclo  tidy
    cbs add-pkg    sclo7-sclo-php56-sclo-candidate --owner=sclo  tidy
    cbs add-pkg    sclo7-sclo-php71-sclo-candidate --owner=sclo  tidy
    cbs add-pkg    sclo7-sclo-php72-sclo-candidate --owner=sclo  tidy

    cbs build      sclo7-sclo-php70-sclo-el7       <above>.src.rpm
    cbs tag-build  sclo7-sclo-php56-sclo-candidate <above build>
    cbs tag-build  sclo7-sclo-php71-sclo-candidate <above build>
    cbs tag-build  sclo7-sclo-php72-sclo-candidate <above build>

    cbs add-pkg    sclo7-sclo-php73-sclo-candidate --owner=sclo  tidy
    cbs build      sclo7-sclo-php73-sclo-el7       <above>.src.rpm
	=> tidy-0.99.0-40.el7.1
