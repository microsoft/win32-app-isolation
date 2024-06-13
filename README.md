# Welcome to the Win32 app isolation repo
Win32 app isolation is a new security feature on Windows that helps contain the damage and safeguard user privacy choices in the event of an 
application compromise. 
Win32 app isolation is built on the foundation of [AppContainers](https://learn.microsoft.com/en-us/windows/win32/secauthz/implementing-an-appcontainer), which offer a security boundary, 
and components that virtualize resources and provide brokered access to other resources. 
This repo contains the documentation and tools to help you isolate your applications.

## Getting started 
* The first step to isolating your application is to package it to run isolated by following the instructions [here](docs/packagingWithVS/packaging-with-visual-studio.md). 
* Once you have your application packaged, use [Application Capability Profiler](docs/profiler/application-capability-profiler.md) to update the application to grant it access to additional resources.
* We also have additional documentation about the [fundamentals](docs/fundamentals) including file access consent.
* You're now ready to deploy and run your application on Windows.

Binaries for the tools used to package applications to run isolated are shared under the [releases](https://github.com/microsoft/win32-app-isolation/releases) section of the repo.

Release notes for supported Windows builds and tools can be found [here](relnotes/windows-release-notes.md).

## Communicating with the team
We'd love to hear your feedback and answer your questions! 
The best way to communicate with the team is through GitHub [discussions](https://github.com/microsoft/win32-app-isolation/discussions)
and [issues](https://github.com/microsoft/win32-app-isolation/issues). 
Please search for similar discussions and issues before creating new ones. 

## Resources
You can find additional information about Win32 app isolation using the following resources: 
* [Win32 app isolation Build session](https://www.youtube.com/watch?v=w6VwHGPz12w&pp=ygUTd2luMzIgYXBwIGlzb2xhdGlvbg%3D%3D&ab_channel=MicrosoftDeveloper)
* [Win32 app isolation blog](https://blogs.windows.com/windowsdeveloper/2023/06/14/public-preview-improve-win32-app-security-via-app-isolation/)

## Contributing
If you would like to contribute to the documentation, please familiarize yourself with the Code of Conduct resources below and submit a pull request.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
