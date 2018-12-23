%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress || :

%define	optroot	/opt
%define	gitbucket_dataroot	/gitbucket

Name:		gitbucket
Summary:	GitHub clone written with Scala.
Version:	4.29.0
Release:	1%{?dist}
License:	ASL 2.0
URL:		https://github.com/gitbucket/gitbucket
Group:		System/Servers
Source0:	https://github.com/gitbucket/gitbucket/releases/download/%{version}/%{name}.war
Source1:	%{name}.service
Source2:	%{name}.sysconf
Source3:	database.conf

%{?systemd_requires}
Requires(pre): shadow-utils

%description

GitBucket is the easily installable GitHub clone written with Scala.

%prep
%setup -T -c

%build
/bin/true

%install
mkdir -vp %{buildroot}%{optroot}/%{name}
mkdir -vp %{buildroot}%{_sharedstatedir}/%{name}
mkdir -vp %{buildroot}%{gitbucket_dataroot}
install -D -m 755 %{SOURCE0} %{buildroot}%{optroot}/%{name}/%{name}.war
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m 644 %{SOURCE3} %{buildroot}%{gitbucket_dataroot}/database.conf

%pre
getent group gitbucket >/dev/null || groupadd -r gitbucket
getent passwd gitbucket >/dev/null || \
  useradd -r -g gitbucket -d %{_sharedstatedir}/gitbucket -s /sbin/nologin \
          -c "GitBucket GitHub clone" gitbucket
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{optroot}/%{name}/%{name}.war
%{_unitdir}/%{name}.service
%config(noreplace) %attr(755, gitbucket, gitbucket) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %attr(700, gitbucket, gitbucket) %{gitbucket_dataroot}/database.conf
%dir %attr(755, gitbucket, gitbucket)%{_sharedstatedir}/gitbucket
%dir %attr(755, gitbucket, gitbucket)%{gitbucket_dataroot}

%changelog
* Sun Dec 2 2018 ymko_diary <ymko_diary.example.com>
- Version bumpto v4.29.0

* Mon Nov 24 2014 Toru Takahashi <torutk at gmail.com>
- Version bump to v2.6

* Sun Nov 09 2014 Toru Takahashi <torutk at gmail.com>
- Version bump to v2.5

* Sun Oct 26 2014 Toru Takahashi <torutk at gmail.com>
- Version bump to v2.4.1

* Mon Jul 21 2014 Toru Takahashi <torutk at gmail.com>
- execute as gitbucket user

* Sun Jul 20 2014 Toru Takahashi <torutk at gmail.com>
- Version bump to v2.1.

* Mon Oct 28 2013 Jiri Tyr <jiri_DOT_tyr at gmail.com>
- Version bump to v1.7.

* Thu Oct 17 2013 Jiri Tyr <jiri_DOT_tyr at gmail.com>
- First build.
